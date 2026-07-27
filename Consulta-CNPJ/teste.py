import time
import pyautogui as py
import pandas as pd
import pdfplumber
import os
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

py.FAILSAFE = True
py.PAUSE = 0.5
site_consulta = "https://www.prt2.mpt.mp.br/servicos/certidao-positiva-negativa"
cnpj_azul = "09.296.295/0001-60"

print("Abrindo site...")
driver = webdriver.Chrome()
driver.get(site_consulta) #Abrindo o site

print("Localizando campo CNPJ...")
campo_cnpj = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "cnpj"))
)
campo_cnpj.send_keys(cnpj_azul)

print("Aperte 'Não sou um Robô'")
time.sleep(100)

print("Localizando campo consultar")
campo_consulta = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.ID, "codin_consultar"))
) 
campo_consulta.click()
print("Irá carregar para a próxima página")
time.sleep(8)

py.press('tab')
py.press("enter")
print("Cheguei na página correta?")

print("Procurando tabala alvo")
print(tabela_alvo.get_attribute("outerHTML"))

linhas = tabela_alvo.find_elements(By.TAG_NAME, "tr")

# for linha in linhas[1:]:  # ignora cabeçalho

#     colunas = linha.find_elements(By.TAG_NAME, "td")

#     ano = colunas[0].text
#     classe = colunas[1].text
#     numero = colunas[2].text
#     parte_passiva = colunas[3].text
#     situacao = colunas[4].text

#     print(
#         ano,
#         classe,
#         numero,
#         parte_passiva,
#         situacao
#     )



time.sleep(40)
input("Teste concluído. Aperte Enter para encerrar.")

