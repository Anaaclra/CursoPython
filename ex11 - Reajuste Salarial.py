#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Digite seu salário R$: '))
aumento = 15
soma = (15/100) * salario
resultado = salario + soma
print('Seu salário é de R$ {}, devido a sua promoção terá um aumento de 15%, sobre o mesmo, totalizando um valor total de salário de R$ {}'.format(salario, resultado))