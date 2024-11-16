#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n1 = int(input('Digite o número desejado: '))
dobro = n1 * 2
triplo = n1 * 3
raiz = n1 ** (1/2)
print('O número escolhido foi {}, \n o seu dobro é {}, \n o seu triplo é {} e, \n sua raiz quadrada é {}'.format(n1, dobro, triplo, raiz))
print('O número escolhido foi {}, \n o seu dobro é {}, \n o seu triplo é {} e, \n sua raiz quadrada é {}'.format(n1, (n1*2), (n1*3), (n1**(1/2))))