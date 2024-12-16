'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

-Até 9 anos: Mirim
-Até 14 anos: Infantil
-Até 19 anos: Junior
-Até 20 anos: Sênior
-Acima: Master'''

print('°•..•'*7)
print('Bem Vindo(a) Confederação de Natação!')
print('°•..•'*7)

idade = int(input('Digite a sua idade para ver em qual categoria você se enquadra: '))

if idade <= 9:
    print('Categoria: Mirim')
elif idade <= 14:
    print('Categoria: Infantil')
elif idade <= 25:
    print('Categoria: Sênior')
else:
    print('Categoria: Master')