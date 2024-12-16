'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

-Média abaixo de 5.0: REPROVADO
-Média entre 5.0 e 6.9: RECUPERAÇÃO
-Média 7.0 ou superior: APROVADO'''

print('°•..•'*2)
print('Média Final')
print('°•..•'*2)

np1 = float(input('Primeira Nota: '))
np2 = float(input('Segunda Nota: '))
resultado = (np1 + np2) / 2

if resultado >= 7.0:
  print('Parabéns, você foi aprovado, sua média foi de {}.'.format(resultado))
elif resultado >= 5.0 or resultado <= 6.9:
  print('Sua média foi de {}, você está de Recuperação'.format(resultado))
elif resultado < 5.0:
  print('Desculpe, mas sua média foi de {}, infelismente você está Reprovado.'.format(resultado))

#Depois tentar verificar do porque com 4.5 o sistema entende que é recuperação e não reprovado.