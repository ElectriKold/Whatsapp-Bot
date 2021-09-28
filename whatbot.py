from selenium import webdriver
import time

class Zapbot:
    def __init__(self):
        self.mensagem = "olá bom dia" #Text Random
        self.grupos = ["Teste 2","Teste para bot de whatzap"]#the groups/people you want to send this mensage
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-pt')#respective language (personal)
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def __enter__(self):
        return self

    def __exit__(self, *_):
        self.driver.close()

    def wait_for_login(self):
        try:
            while self.driver.find_element_by_xpath("//canvas[@aria-label='Scan me!']"):
                time.sleep(1)
        except:
            return

    def send_group_message(self, group: str):
        grupo = self.driver.find_element_by_xpath(f"//span[@title='{group}']")
        grupo.click()
        time.sleep(1)
        chat_box = self.driver.find_element_by_xpath("//div[@class='p3_M1']")
        chat_box.click()
        chat_box.send_keys(self.mensagem)
        enviou_mensagem = self.driver.find_element_by_xpath("//div[@class='_3HQNh _1Ae7k']")
        time.sleep(1)
        enviou_mensagem.click()

    def mensagens_enviar(self):
        self.driver.get('https://web.whatsapp.com/') 
        time.sleep(5)
        self.wait_for_login()

        while True == True: # para verificar sempre verdadeiro
            for grupo in self.grupos:
                self.send_group_message(grupo)


with Zapbot() as bot:
    bot.mensagens_enviar()