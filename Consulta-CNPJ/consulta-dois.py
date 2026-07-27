import pyautogui as py
import time
import pandas as pd
import pdfplumber
import keyboard 
import os

pasta_script = os.path.dirname(os.path.abspath(__file__))

arquivo_pdf = os.path.join(
    pasta_script,
    "src",
    "Certidão de feitos cnpj 09.296.295.0001-60.pdf"
)

with pdfplumber.open(arquivo_pdf) as pdf:
    texto = ""

    for pagina in pdf.pages:
        texto += pagina.extract_text() or ""

print(texto)