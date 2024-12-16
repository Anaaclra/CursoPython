'''Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 

-1 para binário
-2 para octal
-3 para hexadecimal'''

num = int(input('Escreva um número desejado: '))
conversao = int(input('Escolha para qual base você quer converter o número: \n1 - Binário\n2 - Octal\n3 - Hexadecimal\nDigite o número da opção escolhida: '))

if conversao == 1:
  conversao = bin(num)[2:]
  print('O número {} convertido para base Binária é {}'.format(num,conversao))
elif conversao == 2:
  conversao = oct(num)[2:]
  print('O número {} convertido para base Octal é {}'.format(num,conversao))
elif conversao == 3:
  conversao = hex(num)[2:]
  print('O número {} convertido para base Hexadecimal é {}'.format(num,conversao))
else:
  print('Opção Inválida.')
