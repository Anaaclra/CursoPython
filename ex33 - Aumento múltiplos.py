'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
Para salários superiores a R$ 1.250.00, calcule um aumento de 10%.
Para inferiores ou iguais o aumento é de 15%.'''

salario = int(input('Digite o seu salário: '))

if salario > 1250:
  aumento = salario + (salario * 10 / 100)
else:
  aumento = salario + (salario * 15 / 100)

print('Seu aumento foi de R${}.'.format(aumento))