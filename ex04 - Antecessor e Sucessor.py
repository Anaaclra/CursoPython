#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
n1 = int(input('Digite um número: '))
ant = n1 - 1
suc = n1 + 1
print('Você escolheu o número {}, o antecessor deste é {}, e seu sucessor é {}.'.format (n1, ant, suc))
print('Você escolheu o número {}, o antecessor deste é {}, e seu sucessor é {}.'.format (n1, (n1-1), (n1+1)))