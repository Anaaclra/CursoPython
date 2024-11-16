import math
'''num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, math.floor(raiz)))'''

# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

num = float(input('Digite um número: '))
nr = math.trunc(num)
print('O número digitado foi {} e a sua porção inteira é {}'.format(num, nr))
