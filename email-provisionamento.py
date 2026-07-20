##Passo à passo: 
# Entrar no Outlook
# Abrir a planilha
# Conferir campos: ID PROCESSO, NÚMERO e Base Código.
# Ir em novo email
# Selecionar o Para = Renato Mendes 
# Selecionar o Assunto e escrever: PROVISIONAMENTO AUTO DE INFRAÇÃO  - CADASTRADO NO ELAW 
# Selecionar o Campo de texto e escrever: @Renato Mendes da Silva. Segue novo processo cadastrado para provisão no sistema. Base: Att,

import pyautogui as py
import time
import pandas as pd

py.FAILSAFE = True
py.PAUSE = 0.5

## Importar a Planilha de Cadastros
tabela = pd.read_excel("cadastrar.xlsx")
# print(tabela.columns.tolist())
print(tabela)

##Preparando os dados e montando o Email
for linha in tabela.index:
    id_elaw = tabela.loc[linha, "ID Processo"]
    auto_infracao = tabela.loc[linha, "Notificação/Número"]
    base = tabela.loc[linha, "Base Código"]

    titulo = f"PROVISIONAMENTO AUTO DE INFRAÇÃO Nº {auto_infracao} - CADASTRADO NO ELAW {id_elaw}"
    assunto = mensagem = f"""@Renato Mendes da Silva.

    Segue novo processo cadastrado para provisão no sistema.

    Base: {base}

    Att,
    """
    # print ("=" * 50)
    # print (titulo)
    # print (assunto)

################# Entrar no Outlook ######################
#- Abrir o navegador:
py.press("win") # Apertar Tecla Windows
py.write("Outl") # - Procurar o navegador ou programa usado
py.press("enter") # - Apertar Enter para abrir o Aplicativo
time.sleep(5) # tempo para carregar
py.hotkey('win', 'up')

time.sleep(1)
py.hotkey('ctrl', 'n') #Começar a escrever novo Email
