'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$ 7,00 por cada km acima do limite'''

velocidade = float(input('Qual foi a velocidade do carro?(em km/h)'))

excesso = velocidade - 80
multa = excesso * 7.00

if velocidade > 80:
  print('Você está sendo multado no valor de {}.'.format(multa))
else:
  print('Você está dentro do limite, siga adiante!')