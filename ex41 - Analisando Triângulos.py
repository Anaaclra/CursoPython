'''Refaça o DESAFIO 034 dos triângulos  acrescentando o recurso de mostrar que tipo de triângulo será formado: 

- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes'''

a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))

if a < b+c and b < a+c and c < a+b:
    print('É um triangulo')

    if a == b == c: # ou a == b and b == c:
        print('Triângulo Equilatero')

    elif  a != b != c != a:  #ou a != b and b != c and c != a:
        print('Triângulo escaleno')

    elif a < 90 and b < 90 and c < 90:
        print('Triângulo acutângulo')

    elif a == b or b == c or a == c:
        print('Triângulo Isosceles')

else:
    print('Não é um triangulo')