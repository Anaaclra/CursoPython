#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

valor = float(input('Quantos metros deseja?: '))
cm = valor * 100
mm = valor * 1000
print('O Valor desejado foi de {}, convertendo o mesmo para centímetros temos {}, e em milímetros temos {} '.format(valor, cm, mm))