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
import keyboard #a biblioteca keyboard, que fica "escutando" até alguém fazer tal ação desejada

py.FAILSAFE = True
py.PAUSE = 0.7

## Importar a Planilha de Cadastros para noção dos dadaos
tabela = pd.read_excel("provisionamento.xlsx")
print(tabela)

# Entrar no Outlook 
py.press("win") # Apertar Tecla Windows
py.write("Outl") # - Procurar o navegador ou programa usado
py.press("enter") # - Apertar Enter para abrir o Aplicativo
time.sleep(10) # tempo para carregar


## Preparando os itens e Montando o Email
for linha in tabela.index:
    #Variavéis
    id_elaw = tabela.loc[linha, "ID Processo"]
    auto_infracao = tabela.loc[linha, "Notificação/Número"]
    base = tabela.loc[linha, "Base Código"]
    processo = tabela.loc[linha, "Processo"]
    
    
    titulo = f"PROVISIONAMENTO {processo} Nº {auto_infracao} - CADASTRADO NO ELAW {id_elaw}"
    assunto = mensagem = f"""@Renato Mendes da Silva.

    Segue novo processo cadastrado para provisão no sistema.

    Base: {base}

    Att,
    """
    
    time.sleep(5)
    py.hotkey('ctrl', 'n') #Começar a escrever novo Email
    print("Começando a escrever Email")
    py.write("Renato Mendes")
    py.press('enter')
    
    py.press('tab', presses=2)
    py.write(titulo)
    py.press('tab')
    py.write(assunto)
    
    
    print("Esperando verificação para prosseguir!")
    keyboard.wait('ctrl+enter') #Espera até eu verificar o Email e enviar o email pelo atalho, aí reinicia e começa a escrever o próximo Email

    while keyboard.is_pressed('ctrl'):
        time.sleep(0.1)
    time.sleep(0.5)
    
    

print("Emails enviados com sucesso!")
##TESTE 1 - Email 1 enviado com sucesso, pensar em forma de gerar outro assim que enviar o primeiro.

##TESTE 2 - Emails escrevidos com sucesso, porém ao começar o segundo email as letras trocam a de maiusculas para minusculas e o oposto também! Mas foi um sucesso que ele só comece a escrever o próximo Email quando eu enviar (com o atalho Ctrl + Enter)

##TESTE 3 - Emais ainda são enviados com sucesso, compreendi o erro que ocorreu no teste 2, em determinado momento eu ligo o botão escrito "fixa" que ocorre o reverter das letras no teste 2, então eu percebi que esse é oq pega, mas a automação ainda é muito útil, só me atentar nesse detalhe

##TESTE 4 - Email enviados com sucesso!


