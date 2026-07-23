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
from selenium.webdriver.support.ui import Select
import os


select = Select(driver.find_element("id", "estado"))
select.select_by_visible_text("São Paulo")

site_consulta = "https://www.prt2.mpt.mp.br/servicos/certidao-positiva-negativa"

driver = webdriver.Chrome()

driver.get(site_consulta)



##Substituição do Time.sleep:
campo = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.NAME, "cnpj")
    )
)

arquivo = os.path.exists("certidao.pdf") #Forma de Verificar se o Documento foi baixado!