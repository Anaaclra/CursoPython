#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
n1 = int(input('Digite um número desejado: '))

print('A tabuada do {}, é'.format(n1))

print('-' * 12)
print(n1,'x 1 =',n1 * 1)
print(n1,'x 1 =',n1 * 2)
print(n1,'x 1 =',n1 * 3)
print(n1,'x 1 =',n1 * 4)
print(n1,'x 1 =',n1 * 5)
print(n1,'x 1 =',n1 * 6)
print(n1,'x 1 =',n1 * 7)
print(n1,'x 1 =',n1 * 8)
print(n1,'x 1 =',n1 * 9)
print(n1,'x 1 =',n1 * 10)

#or

print('-' * 12)
print('{} x {} = {}'.format(n1, 1, n1*1))
print('{} x {} = {}'.format(n1, 2, n1*2))
print('{} x {} = {}'.format(n1, 3, n1*3))
print('{} x {} = {}'.format(n1, 4, n1*4))
print('{} x {} = {}'.format(n1, 5, n1*5))
print('{} x {} = {}'.format(n1, 6, n1*6))
print('{} x {} = {}'.format(n1, 7, n1*7))
print('{} x {} = {}'.format(n1, 8, n1*8))
print('{} x {} = {}'.format(n1, 9, n1*9))
print('{} x {} = {}'.format(n1, 10, n1*10))
print('-' * 12)
