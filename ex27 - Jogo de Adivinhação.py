'''Escreva um programa que faça o computador pensar entre um número inteiro de 0 a 5 e peça para o usário tentar descobrir qual foi o número escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu'''

import random

computador = random.randint(0, 5)

print('Bem vindo(a), o computador irá escolher um número.')
usuario = int(input('Escolha um número de 0 á 5 e tente acertar qual é foi escolhido pelo o computador: '))

if usuario == computador:
  print('Parabéns, você acertou o número escolhido pelo computador!!!', computador)
else:
  print('Tente novamente!, o número escolhido foi', computador)