from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException

#projeto feito com chromedriver, baixe o webdriver do navegador que você utiliza
#https://chromedriver.chromium.org/downloads link chromedriver

#coloque o caminho onde está o executavel do webdriver
CHROME_DRIVER_PATH = r"#"

#informe seu login e senha
USERNAME = "#"
PASSWORD = "#"


#Classe de execução do programa
class InstaFollower():

    def __init__(self, driver_path):
        #executa o webdriver
        self.driver = webdriver.Chrome(executable_path=driver_path)
        #passa o link para logar no instagram
        self.driver.get("https://www.instagram.com/accounts/login/")
        #maximiza a pagina
        self.driver.maximize_window()

    #Método para logar na conta do intagram
    ################ ALERTA ##################
    #Caso de erro nessa função é possivel que tenha tido alguma atualização na pagina do instagram e os caminhos dos elementos xpath foram alterados
    #SOLUÇÃO: entre no link vá em inspecionar ache o botão e click com botão direito para copiar o xpath
    def login(self):
        #É utilizado o sleep para o carregamento da pagina, caso de algum erro por carregamento, aumento o sleep()
        sleep(2)

        #Pega o xpath da pagina de login e preenche com o seu login
        self.username = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input")
        self.username.send_keys(USERNAME)

        # Pega o xpath da pagina de login e preenche com a sua senha
        self.password = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input")
        self.password.send_keys(PASSWORD)

        #Confirma o login para entrar
        sleep(1)
        self.enter = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]/button/div")
        self.enter.click()

        #clicka no Botão para não salvar informações de login
        sleep(3)
        self.button_agora_nao_salvar_info = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
        self.button_agora_nao_salvar_info.click()

        #clica no Botão para não ter notificações
        sleep(1)
        self.button_agora_nao_notificacoes = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
        self.button_agora_nao_notificacoes.click()

    #Método para seguir os Perfis do úsuario desejado
    ################ ALERTA ##################
    # Caso de erro nessa função é possivel que tenha tido alguma atualização na pagina do instagram e os caminhos dos elementos xpath foram alterados
    # SOLUÇÃO: entre no link vá em inspecionar ache o botão e click com botão direito para copiar o xpath
    def find_followers(self):
        #Coloque aqui o link do perfil para que o seu perfil siga os perfis que seguem essa conta
        self.driver.get("https://www.instagram.com/axiafutures/")

        #Vai até seguidores do perfil selecionado.
        sleep(1)
        self.seguidores = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
        self.seguidores.click()

        #Click para seguir 10 perfis do perfil selecionado
        #Instagram tem limitador de perfis que pode seguir, coloquei 10, mas acredito que até 100 é permitido, caso queira alterar mude o range()
        sleep(2)
        modal = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        for i in range(10):

            #Chama o método para seguir o perfil
            instafollower.follow()
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(2)

        ###################### Caso apareça algum popup descomente essa parte do código ###################
        # self.popup = self.driver.find_element_by_xpath("/html/body/div[5]/div/div")
        # self.popup.send_keys(Keys.END)
        ###################### Caso queira seguir um numero mair de perfis que aparecem na tela, descomente esse código para fazer o scroll ###################
        # self.src1 = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")
        # self.scroll = self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", self.src1)

    #Método que segue o perfil
    #Possui um tratamento de erro para caso já siga o perfil selecionado
    #Vai tentar seguir, caso de erro irá cancelar e irá para o proximo perfil
    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/button[2]")
                cancel_button.click()
        return

#objeto da classe InstaFollower
instafollower = InstaFollower(CHROME_DRIVER_PATH)

#objeto chama método para logar na conta
instafollower.login()

#objeto chama o método para seguir pefil
instafollower.find_followers()

