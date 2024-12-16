'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo: 

-Abaixo de 18.5: Abaixo do Peso
-Entre 18.5 e 25: Peso ideal
-25 até 30: Sobrepeso
-30 até 40: Obesidade
-Acima de 40: Obesidade mórbida'''

print ("Bem vindo a Calculadora de IMC")

pergunta_nome = input("Qual é o seu nome? " )
nome = ("Olá" , pergunta_nome)
idade = input (f"Qual sua idade? ")
peso = float(input("Qual seu peso (em KG)? "))
altura = float(input("Qual sua Altura (em metros e usando ponto)? "))

print("Vamos calcular seu IMC")

imc = (peso / (altura * altura))

print(pergunta_nome , (f"seu IMC é: {imc:.2f}"))

if imc < 18.5:
	print("Seu estado é Abaixo do Peso\nPrecisa rever sua alimentação.")
elif imc >= 18.5 and imc <= 25:
	print("Seu estado é Peso ideal")
elif imc >= 30:
	print("Seu estado é de Sobrepeso\nPrecisa rever sua alimentação.")
elif imc >= 35:
	print("Seu estado é de Obesidade Grau I\nProcure um médico ou nutricionista.")
elif imc >= 40:
	print("Seu estado é de Obesidade Grau II (severa)\nProcure um médico ou nutricionista.")
else:
	print("Seu estado é de Obesidade Grau III (mórbida)\nProcure um médico ou nutricionista.")