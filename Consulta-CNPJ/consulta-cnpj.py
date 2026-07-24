#Passo À Passo: 

##### 1 - PEGAR O DOCUMENTO 
# a - Entrar no site de Consulta MPT ---
# b - Adicionar o CNPJ no campo requisitante
# c - Confirmar "Não sou um Robô"
# d - Clicar em conssultar
# e - Imprimir como PDF
# f - Inserir Nome do PDF e salvar 

###### 2 - LER O DOCUMENTO E TRANSFERIR INFORMAÇÕES
# a - Ler informações e ignorar o documento até começar a tabela
# b - Ler informações da tabela e inserir em uma planilha vazia
# c - Repetir o processo de leitura até acabar a planilha do documento

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
time.sleep(50)

print("Localizando campo consultar")
campo_consulta = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.ID, "codin_consultar"))
) 
campo_consulta.click()
print("Botão consulta clicado! Irá carregar para a próxima página")
time.sleep(5)

botao_imprimir = driver.execute_script("""
return document.querySelector('print-preview-app')
.shadowRoot.querySelector('print-preview-sidebar')
.shadowRoot.querySelector('cr-button.action-button');
""")

print(botao_imprimir)

# print("Localizando campo imprimir para guardar PDF")
# campo_imprimir = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CLASS_NAME, "action-button"))
# )
# campo_imprimir.click()
# print("Botão imprimir clicado! Aguardando download")

# Certificação da onde o documento será baixado (dentro da pasta da automação)
# pasta_download = os.path.dirname(os.path.abspath(__file__))

# cnpj_arquivo = cnpj_azul.replace("/", "-")
# nome_arquivo = f"certidao de feitos cnpj {cnpj_arquivo}.pdf"

# caminho_arquivo = os.path.join(
#     pasta_download,
#     nome_arquivo
# )

# Digita o caminho completo na janela "Salvar como"
# py.write(caminho_arquivo)
# py.press("enter")


# time.sleep(3)  
# if os.path.exists(caminho_arquivo):
#     print("Arquivo encontrado!")
# else:
#     print("Arquivo NÃO encontrado!")

time.sleep(40)
input("Teste concluído. Aperte Enter para encerrar.")


##CONCLUSÃO TESTES ATÉ 24/07 às 13H --> O programa está entrando no site desejado e conseguindo acessar ele, ele aperta o botão consultar e então ao abrir a nova tela, para imprimir o arquivo, ele não consegue localizar o Botão Imprimir para baixar o arquivo.. fiz mais alguns passos avançados mas não chega nem a rodar por conta dessa falha.