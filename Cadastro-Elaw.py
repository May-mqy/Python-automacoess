import pyautogui as py
import time
import pandas as pd

link = "https://azul.elaw.com.br/"
py.PAUSE = 0.5

################# PASSO 1 - Entrar no Sistema da Elaw ######################
# - Abrir o navegador:
py.press("win") # Apertar Tecla Windows
py.write("Edge") # - Procurar o navegador ou programa usado
py.press("enter") # - Apertar Enter para abrir o Aplicativo
time.sleep(5) # tempo para carregar 
py.hotkey('ctrl', 'l')   # seleciona a barra de endereço
py.write(link)
py.press('enter')
time.sleep(5)
py.press("tab") # Entrar com a credencial
py.press("enter")
time.sleep(5)


########### Abrir a base de dados
# - Importar o arquivo
#tabela = pd.read_csv("") #Incluir tabela atualizada para novos cadastros
#print(tabela)