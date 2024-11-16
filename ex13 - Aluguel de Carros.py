#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input("Quantidade de Km percorridos: "))
dias = int(input("Quantidade de dias de aluguel: "))
alu_por_dia = dias*60
rod_por_km = 0.15*km
total_pago = alu_por_dia + rod_por_km
print('O total a pagar é de R${:.2f}'.format(total_pago))