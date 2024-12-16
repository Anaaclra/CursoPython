'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

-À vista dinheiro/cheque: 10% de desconto.
-À vista no cartão: 5% de desconto.
-em até 2x no cartão: Preço normal.
-3x ou mais no cartão 20% de juros.'''

produto = float(input('Qual o valor do produto? R$' ))
pagamento = int(input('Qual vai ser a forma de pagamento do produto? (Escolha o número da opção desejada)\n1 - À vista dinheiro/cheque\n2 - À vista no cartão\n3 - Em até 2x no cartão\n4 - 3x ou mais no cartão - '))



if pagamento == 1:
  produto = produto * (10 / 100)
  print('Seu produto teve um desconto de R${}.'.format(produto))
elif pagamento == 2:
  produto = produto * (5 / 100)
  print('Seu produto teve um desconto de R${}.'.format(produto))
elif pagamento == 3:
  print('Seu produto ficou no total de R${}.'.format(produto))
elif pagamento == 4:
  produto = produto + (produto * 20 / 100)
  print('Seu produto ficou no total de R${}.'.format(produto))