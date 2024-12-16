'''Escreva um programa que leia dois números inteiros compare-os, mostrando na tela uma mensagem:

-O primeiro valor é maior
-O segundo valor é maior
-Não existe valor maior, os dois são iguais'''

num1 = int(input('Digite o primeiro número desejado: '))
num2 = int(input('Digite o segundo número desejado: '))

if num1 > num2:
  print('O valor {} é maior que {}. '.format(num1, num2))
elif num2 > num1:
  print('O valor {} é maior que {}.'.format(num2, num1))
else:
  print('Não existe valor maior ou menor, os dois números são iguais!!!')