'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.'''

valor_da_casa = float(input('Digite o valor da casa desejada R$ '))
salario = float(input('Digite seu salário atual R$'))
anos = int(input('Digite em quantos anos deseja quitar a casa: '))
prestacao = valor_da_casa / (anos * 12)
print('Com base no seu salário e o valor do imóvel desejado, sua prestação ficará no valor de R${}'.format(prestacao))

if prestacao <= 0.3 * salario:
  print('Parabéns seu empréstimo foi aceito!!!')
else:
  print ('Sinto Muito, mas seu empréstimo não foi aceito, pois 30% do seu salário é R${}.'.format(salario * 0.3))