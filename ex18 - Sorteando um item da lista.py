#Um professor quer sortear um de seus quatro alunos para apagar o quadro. Faça um programa que ajude a ele, lendo o nome deles e escrevendo o nome do escolhido.

import random
aluno1 = input("Digite o nome do primeiro aluno:")
aluno2 = input("Digite o nome do segundo aluno:")
aluno3 = input("Digite o nome do terceiro aluno:")
aluno4 = input("Digite o nome do quarto aluno:")
lista=[aluno1,aluno2,aluno3,aluno4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))