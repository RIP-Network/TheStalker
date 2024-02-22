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
    print("")
    account=input(azul + "[*] ID directo del chat ( ejem : 17842098713946889 ) : " + cierre)

    with open("Cookies/cookie1.txt", "r") as file:
        cookie_data = file.readline().strip().split('\t')

    cookie = {
        'name': cookie_data[0],
        'value': cookie_data[1],
        'domain': cookie_data[2],
        'path': cookie_data[3],
        'expiry': cookie_data[4],
        'secure': cookie_data[5],
        'httpOnly': cookie_data[6]
}

    driver = webdriver.Chrome()

    driver.get(f"https://www.instagram.com/direct/t/{account}/") 
    time.sleep(4)
    driver.add_cookie(cookie)
    time.sleep(2)

    driver.refresh()
    time.sleep(4)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]').send_keys("RIP-Network bot V1 Has Here.")
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[3]').send_keys(Keys.RETURN)
    time.sleep(2)
    driver.quit()

    with open("Cookies/cookie2.txt", "r") as file:
        cookie_data = file.readline().strip().split('\t')

    cookie = {
        'name': cookie_data[0],
        'value': cookie_data[1],
        'domain': cookie_data[2],
        'path': cookie_data[3],
        'expiry': cookie_data[4],
        'secure': cookie_data[5],
        'httpOnly': cookie_data[6]
}

    driver = webdriver.Chrome()

    driver.get(f"https://www.instagram.com/direct/t/{account}/") 
    time.sleep(4)
    driver.add_cookie(cookie)
    time.sleep(2)

    driver.refresh()
    time.sleep(4)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]').send_keys("RIP-Network bot V1 Has Here.")
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[3]').send_keys(Keys.RETURN)
    time.sleep(2)
    driver.quit()

    with open("Cookies/cookie3.txt", "r") as file:
        cookie_data = file.readline().strip().split('\t')

    cookie = {
        'name': cookie_data[0],
        'value': cookie_data[1],
        'domain': cookie_data[2],
        'path': cookie_data[3],
        'expiry': cookie_data[4],
        'secure': cookie_data[5],
        'httpOnly': cookie_data[6]
}

    driver = webdriver.Chrome()

    driver.get(f"https://www.instagram.com/direct/t/{account}/") 
    time.sleep(4)
    driver.add_cookie(cookie)
    time.sleep(2)

    driver.refresh()
    time.sleep(4)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]').send_keys("RIP-Network bot V1 Has Here.")
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[3]').send_keys(Keys.RETURN)
    time.sleep(2)
    driver.quit()

def social_falsification():
    print("")
    account=input(azul + "[*] ID directo del chat ( ejem : 17842098713946889 ) : " + cierre)

    with open("Cookies/cookie1.txt", "r") as file:
        cookie_data = file.readline().strip().split('\t')

    cookie = {
        'name': cookie_data[0],
        'value': cookie_data[1],
        'domain': cookie_data[2],
        'path': cookie_data[3],
        'expiry': cookie_data[4],
        'secure': cookie_data[5],
        'httpOnly': cookie_data[6]
}

    driver = webdriver.Chrome()

    driver.get(f"https://www.instagram.com/direct/t/{account}/") 
    time.sleep(4)
    driver.add_cookie(cookie)
    time.sleep(2)

    driver.refresh()
    time.sleep(4)
    os.system('clear')
    print(azul + "[*] Sesion establecida con exito." + cierre)

def account_osint_simple():
    print("")
    account=input(azul + "[*] Usuario sin el @ ( ejem : ripnetworkyt ) : " + cierre)

    with open("Cookies/cookie1.txt", "r") as file:
        cookie_data = file.readline().strip().split('\t')

    cookie = {
        'name': cookie_data[0],
        'value': cookie_data[1],
        'domain': cookie_data[2],
        'path': cookie_data[3],
        'expiry': cookie_data[4],
        'secure': cookie_data[5],
        'httpOnly': cookie_data[6]
}

    driver = webdriver.Chrome()

    driver.get(f"https://www.instagram.com/{account}") 
    time.sleep(4)
    driver.add_cookie(cookie)
    time.sleep(2)

    driver.refresh()
    time.sleep(4)
    os.system('clear')
    print(azul + "[*] Sesion establecida con exito." + cierre)




def menu():
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
    print(azul + "Created by RIP-Network                   Version 1.0" + cierre)
    print("")
    print(azul + "1. Masive DM Spam: Spam hacia una cuenta Publica/Privada." + cierre)
    print(azul + "2. Ingieneria Social: Suplantar identidad de una cuenta." + cierre)
    print(azul + "3. OSINT: Reconocimiento basico sobre una cuenta publica" + cierre)
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
    elif opcion == "5":
        webbrowser.open('https://github.com/RIP-Network/TheStalker/issues')
    elif opcion == "6":
        os.system('clear')
        print(azul + "Saliendo, Gracias por usar." + cierre)
    else:
        os.system('clear')
        print(azul + "[*] No es una opcion valida." + cierre)

if __name__ == "__main__":
    menu()