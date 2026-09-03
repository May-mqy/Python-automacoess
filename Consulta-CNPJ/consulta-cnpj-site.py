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
cnpj_arquivo = cnpj_azul.replace("/", "-")

print("Abrindo site...")
driver = webdriver.Chrome()
driver.get(site_consulta) #Abrindo o site'

print("Localizando campo CNPJ...")
campo_cnpj = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "cnpj"))
)
campo_cnpj.send_keys(cnpj_azul)

print("Aperte 'Não sou um Robô'")
# input("Pressione enter para continuar")
time.sleep(60)

print("Localizando campo consultar")
campo_consulta = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.ID, "codin_consultar"))
) 

campo_consulta.click()
print("Irá carregar para a próxima página")
time.sleep(8)

## PARA ACHAR O CÓDIGO DA TELA ONDE A APLICAÇÃO PASSOU
# print(driver.window_handles)
# print(len(driver.window_handles))


py.press('enter')
print("Indo para a Tela de Baixar Arquivo")
py.press('tab')
py.press('enter')

print("Abas abertas:")
for i, aba in enumerate(driver.window_handles):
    driver.switch_to.window(aba)

    print(f"\nABA {i}")
    print("Título:", driver.title)
    print("URL:", driver.current_url)
    
# Forçando o SELENIUM a ir para a página da Tabela
driver.switch_to.window(driver.window_handles[-1])

print(driver.title)
print(driver.current_url)

#Para verificar se a automação está achando a tabela.. resultado esperado: Tabelas esperadas: 1
tabelas = driver.find_elements(By.TAG_NAME, "table")

print("Tabelas encontradas:", len(tabelas))

# print("Procurando página atual com ajuda INSTRUÇÕES DO COPILOT:")
# print(driver.current_url)
# print(driver.title)

# with open("pagina.html", "w", encoding="utf-8") as arquivo:
#     arquivo.write(driver.page_source)
    
#     print("URL:", driver.current_url)
# print("Título:", driver.title)

# tables = driver.find_elements(By.TAG_NAME, "table")
# print("Quantidade de tabelas:", len(tables))

# # Capturando a tabela do site 
# print("Localizando tabela do site")
# tabela = driver.find_element(By.TAG_NAME, "table")

# ###### SEPARAÇÃO DA TABELA COM O PANDAS
# html = driver.page_source

# tabelas = pd.read_html(html)

# df = tabelas[0]

# df.to_excel(
#     "Certidao_MPT.xlsx",
#     index=False
# )

###### SEPARAÇÃO DA TABELA COM O SELENIUM
# # Capturando Linhas e Colunas
# time.sleep(40)
# input("Teste concluído. Aperte Enter para encerrar.")
# linhas = tabela.find_elements(By.TAG_NAME, "tr")

# dados = []

# for linha in linhas:
#     colunas = linha.find_elements(By.TAG_NAME, "td")

#     if colunas:  # ignora cabeçalho
#         dados.append([
#             coluna.text.strip()
#             for coluna in colunas
#         ])
        
# cabecalho = [
#     th.text.strip()
#     for th in tabela.find_elements(By.TAG_NAME, "th")
# ]

# df = pd.DataFrame(
#     dados,
#     columns=cabecalho
# )