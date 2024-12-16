#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero = int(input('Digite um número: '))

if numero % 2 == 0:
  print('O número escolhido é PAR')
else:
  print('O número escolhido é ÍMPAR')