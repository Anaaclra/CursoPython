#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo, calcule e mostre o comprimento da hipotenusa.
import math
'''co = float(input('Digite a largura do Cateto oposto: '))
ca = float(input('Digite a largura do Cateto adjacente: '))
hi = (ca ** 2 + co ** 2) ** (1/2)
print("O comprimento da hipotenusa é {} ".format(hi))'''

co = float(input('Digite a largura do Cateto oposto: '))
ca = float(input('Digite a largura do Cateto adjacente: '))
hi = math.hypot(co, ca)
print("O comprimento da hipotenusa é {:.2f} ".format(hi))