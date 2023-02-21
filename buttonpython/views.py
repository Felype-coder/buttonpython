from selenium.webdriver.common.by import By
from django.http import HttpResponse
from django.shortcuts import render
from selenium import webdriver
from time import sleep
import pyautogui



def button(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == 'POST':
        return HttpResponse(HttpResponse, 'index.html')


def output(request):
    while True:
        if request.method == 'GET':
            # grupo temporario para testes ->>>> https://chat.whatsapp.com/BvgLZiOp3OEIAAITBiJS8L
            # grupo alvo do script ->>>>>  https://chat.whatsapp.com/D994NUZj0dwL2Z17qfGDyg
            # Escolhendo o site que o navegador abrira

            driver = webdriver.Chrome(executable_path=r'buttonpython/chromedriver.exe')
            driver.get('https://chat.whatsapp.com/BvgLZiOp3OEIAAITBiJS8L')
            sleep(9)

            # primeiro clique entrar na conversa

            sleep(6)  # Lembrando que o temporizador e extremamente importante para pipeline
            entrar_na_conversa = driver.find_element(By.XPATH, '//*[@id="action-button"]')
            sleep(5)
            entrar_na_conversa.click()

            sleep(11)
            # Use o whatsapp aberto
            whatsapp_aberto = driver.find_element(By.XPATH, '//*[@id="fallback_block"]/div/h4/a/span')
            sleep(10)
            whatsapp_aberto.click()

            # Aqui nessa parte o whatsapp ira pedir a autentificação
            sleep(25)
            entrar_no_grupo = driver.find_element(By.XPATH,
                                                  '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div[2]/div/div[2]/div/div')
            entrar_no_grupo.click()

            sleep(35)
            tipo_Arquivo_envio = driver.find_element(By.XPATH,
                                                     '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/span')
            tipo_Arquivo_envio.click()

            sleep(11)
            selecionado_documento = driver.find_element(By.XPATH,
                                                        '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[4]/button/span')
            selecionado_documento.click()
            sleep(11)

            documentos = ['Linux_Atividade_2_Comandos_e_Shell', 'financas',
                          'GestorOnline']  # arquivos para serem enviados

            # aqui fica a parte principal do codigo o looping periodizado por assim dizer
            try:
                for arquivo in arquivos:  # aqui tentarei
                    sleep(5)
                    pyautogui.write(arquivo)
                    sleep(11)
                    sleep(11)  # temporizador extremamente importante
                    pyautogui.press("Enter")
                    sleep(5)
                    clicar_cruz = driver.find_element(By.CSS_SELECTOR,
                                                      "#app > div > div > div._2QgSC > div._2Ts6i._2xAQV > span > div > span > div > div > div.g0rxnol2.thghmljt.p357zi0d.rjo8vgbg.ggj6brxn.f8m0"
                                                      "rgwh.gfz4du6o.r7fjleex.bs7a17vp.ov67bkzj > div > div.O2_ew > div.p357zi0d.ktfrpxia.nu7pwgvd.ac2vgrno.sap93d0t.r15c9g6i.YB9dD > button")

                    clicar_cruz.click()





            finally:
                sleep(30)

                seta_envio = driver.find_element(By.XPATH,
                                                 '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div')

                seta_envio.click()
                sleep(2)
                pyautogui.press("Esc")

                sleep(1)





        elif request.method == 'POST':

            return HttpResponse(HttpResponse, 'index.html')
