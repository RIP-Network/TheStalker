from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import webbrowser
from time import sleep
import time
import os

negro = '\033[30m'
rojo = '\033[31m'
verde = '\033[32m'
amarillo = '\033[33m'
azul = '\033[34m'
rosado = '\033[35m'
calipso= '\033[36m'
blanco = '\033[37m'
cierre = '\033[39m'

def massive_spam_dm():
    print(azul + "[*] Proximamente." + cierre)
    time.sleep(5)
    os.system('clear')

def account_osint_simple():

    account=input(azul + "[*] Usuario de la cuenta sin el @ ( ejem ripnetworkyt ) : " + cierre)

    def cargar_cookies_json(driver, cookies):
        for cookie in cookies:
            driver.add_cookie(cookie)

    def iniciar_sesion(url, cookies):
        driver = webdriver.Chrome()
        driver.get(url)
    
        cargar_cookies_json(driver, cookies)
    
        driver.refresh()
        input(azul + "[*] Ahora puede revisar la cuenta, estas en modo incognito. Pulse Enter para cerrar." + cierre)
        driver.quit()
        os.system('clear')

    if __name__ == "__main__":
        url = f"https://www.instagram.com/{account}"
    
        cookies = [
            {"domain":".instagram.com","path":"/","name":"datr","value":""},
            {"domain":".instagram.com","path":"/","name":"shbts","value":""},
            {"domain":".instagram.com","path":"/","name":"ds_user_id","value":""},
            {"domain":".instagram.com","path":"/","name":"shbid","value":""},
            {"domain":".instagram.com","path":"/","name":"csrftoken","value":""},
            {"domain":".instagram.com","path":"/","name":"ig_did","value":""},
            {"domain":".instagram.com","path":"/","name":"mid","value":""},
            {"domain":".instagram.com","path":"/","name":"sessionid","value":""},
            {"domain":".instagram.com","path":"/","name":"rur","value":""}
        ]
    
        iniciar_sesion(url, cookies)

def social_falsification():

    account=input(azul + "[*] ID del chat de la cuenta ( ejem 17842098713946889 ) : " + cierre)

    def cargar_cookies_json(driver, cookies):
        for cookie in cookies:
            driver.add_cookie(cookie)

    def iniciar_sesion(url, cookies):
        driver = webdriver.Chrome()
        driver.get(url)
    
        cargar_cookies_json(driver, cookies)
    
        driver.refresh()
        input(azul + "[*] Tienes una cuenta falsificada creible, puedes empezar la ingieneria social, Pulse enter para cerrar" + cierre)
        driver.quit()
        os.system('clear')

    if __name__ == "__main__":
        url = f"https://www.instagram.com/direct/t/{account}"
    
        cookies = [
            {"domain":".instagram.com","path":"/","name":"datr","value":""},
            {"domain":".instagram.com","path":"/","name":"shbts","value":""},
            {"domain":".instagram.com","path":"/","name":"ds_user_id","value":""},
            {"domain":".instagram.com","path":"/","name":"shbid","value":""},
            {"domain":".instagram.com","path":"/","name":"csrftoken","value":""},
            {"domain":".instagram.com","path":"/","name":"ig_did","value":""},
            {"domain":".instagram.com","path":"/","name":"mid","value":""},
            {"domain":".instagram.com","path":"/","name":"sessionid","value":""},
            {"domain":".instagram.com","path":"/","name":"rur","value":""}
        ]
    
        iniciar_sesion(url, cookies)



def menu():
    while True:
         
     os.system('clear')
     print(azul + "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡀⠀⠀⢀⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀" + cierre)
     print(azul + "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣤⣤⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀" + cierre)
     print(azul + "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀" + cierre)
     print(azul + "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⢿⣿⣿⣿⣿⣿⣿⡿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀" + cierre)
     print(azul + "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⠀⣶⣤⣄⣉⣉⣉⣉⣠⣤⣶⠀⣄⣀⡀⠀⠀⠀⠀⠀⠀" + cierre)
     print(azul + "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣾⣿⣿⣿⣿⣦⣄⣉⣙⣛⣛⣛⣛⣋⣉⣠⣴⣿⣿⣿⣿⣷⣶⠀⠀⠀" + cierre)
     print(azul + "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠛⠛⠛⠻⠿⠿⠿⠿⠿⠿⠿⠿⠟⠛⠛⠛⠉⠉⠁⠀⠀⠀⠀" + cierre)
     print(azul + "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⣆⠀⠀⠀⢠⡄⠀⠀⠀⣰⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀" + cierre)
     print(azul + "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⣾⣿⡆⠸⣿⣶⣶⣾⣿⣿⣷⣶⣶⣿⠇⢰⣿⣷⣶⣄⡀⠀⠀⠀" + cierre)
     print(azul + "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠺⠿⣿⣿⣿⣿⣿⣄⠙⢿⣿⣿⣿⣿⣿⣿⡿⠋⣠⣿⣿⣿⣿⣿⠿⠗⠀⠀" + cierre)
     print(azul + "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣷⡄⠈⠙⠛⠛⠋⠁⢠⣾⣿⣿⣿⠟⠋⠀⠀⠀⠀⠀" + cierre)
     print(azul + "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣬⣿⣿⣿⣇⠐⣿⣿⣿⣿⠂⣸⣿⣿⣿⣥⣤⣀⠀⠀⠀⠀⠀" + cierre)
     print(azul + "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠻⠿⠿⢿⣿⣿⣿⣧⠈⠿⠿⠁⣼⣿⣿⣿⡿⠿⠿⠟⠃⠀⠀⠀⠀" + cierre)
     print(azul + "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢿⠀⣶⣦⠀⡿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀" + cierre)
     print(azul + "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀" + cierre)
     print(azul + " ▄▄▄▄▄ ▄ .▄▄▄▄ .    .▄▄ · ▄▄▄▄▄ ▄▄▄· ▄▄▌  ▄ •▄ ▄▄▄ .▄▄▄   " + cierre)
     print(azul + "• ██  ██▪▐█▀▄.▀·    ▐█ ▀. •██  ▐█ ▀█ ██•  █▌▄▌▪▀▄.▀·▀▄ █· " + cierre)
     print(azul + " ▐█.▪██▀▐█▐▀▀▪▄    ▄▀▀▀█▄ ▐█.▪▄█▀▀█ ██▪  ▐▀▀▄·▐▀▀▪▄▐▀▀▄   " + cierre)
     print(azul + " ▐█▌·██▌▐▀▐█▄▄▌    ▐█▄▪▐█ ▐█▌·▐█ ▪▐▌▐█▌▐▌▐█.█▌▐█▄▄▌▐█•█▌ " + cierre)
     print(azul + " ▀▀▀ ▀▀▀ · ▀▀▀      ▀▀▀▀  ▀▀▀  ▀  ▀ .▀▀▀ ·▀  ▀ ▀▀▀ .▀  ▀  " + cierre)
     print("")
     print(azul + "Created by RIP-Network                   Version 1.2" + cierre)
     print("")
     print(azul + "1. Masive DM Spam: Spam hacia una cuenta Publica/Privada." + cierre)
     print(azul + "2. Ingieneria Social: Suplantar identidad de una cuenta." + cierre)
     print(azul + "3. OSINT: Reconocimiento basico sobre una cuenta publica." + cierre)
     print("")
     print(azul + "4. Calificar: Apoya la herramienta con una estrella en GitHub." + cierre)
     print(azul + "5. Comentar error: Comenta cualquier error que hayas encontrado." + cierre)
     print("")
     print(azul + "6. Exit")
     print("")

     opcion = input(azul + "C:\RIP-Network@root > " + cierre)

     if opcion == "1":
             massive_spam_dm()
     elif opcion == "2":
             social_falsification()
     elif opcion == "3":
             account_osint_simple()
     elif opcion == "4":
             webbrowser.open('https://github.com/RIP-Network/TheStalker')
             os.system('clear')
     elif opcion == "5":
             webbrowser.open('https://github.com/RIP-Network/TheStalker/issues')
             os.system('clear')
     elif opcion == "6":
         os.system('clear')
         print(azul + "[*] Saliendo, Gracias por usar." + cierre)
         break 
     else:
         os.system('clear')
         print(azul + "[*] No es una opcion valida vuelvalo a intentar." + cierre)
         time.sleep(3)
         os.system('clear')

if __name__ == "__main__":
    menu()