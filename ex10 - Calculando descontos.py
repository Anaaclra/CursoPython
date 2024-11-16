#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
produto = float(input('Digite o valor do produto: '))
desc = 5
valor = (desc/100) * produto
resultado = produto - valor
print('O Valor do produto é de R$ {}, com desconto de 5%, o desconto sairá por {}%, totalizando o valor de R$ {}'.format(produto, valor, resultado))