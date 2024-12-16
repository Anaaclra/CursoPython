#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

from datetime import datetime

ano = int(input("Digite um ano para verificar se é bissexto (ou 0 para analisar o ano atual): "))

if ano == 0:
    ano = datetime.now().year  

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é BISSEXTO.")
else:
    print(f"O ano {ano} NÃO é BISSEXTO.")