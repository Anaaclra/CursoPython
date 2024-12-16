#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200 km e R$ 0,45 para viagens mais longas.

viagem = float(input('Informe a distância da viagem (em Km): '))

if viagem <= 200:
  preço1 = viagem * 0.50
  print('Sua viagem está custando o total de R$ {}'.format(preço1))
else:
  preço2 = viagem * 0.45
  print('Sua viagem está custando o total de R$ {}'.format(preço2))