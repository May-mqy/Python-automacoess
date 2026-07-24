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

import pandas as pd
import pdfplumber
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


site_consulta = "https://www.prt2.mpt.mp.br/servicos/certidao-positiva-negativa"

driver = webdriver.Chrome()
driver.get(site_consulta) #Abrindo o site


campo_cnpj = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "cnpj"))
)
campo_cnpj.send_keys("09.296.295/0001-60")


##Substituição do Time.sleep:
campo = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.NAME, "cnpj")
    )
)

arquivo = os.path.exists("certidao.pdf") #Forma de Verificar se o Documento foi baixado!