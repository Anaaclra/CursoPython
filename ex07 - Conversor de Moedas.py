#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
p = float(input('Quantos R$ você tem guardado no momento?: '))
dolar = 5.43
resultado = p / dolar
print ('Atualmente você tem R$ {}, que convertendo para dolar você consegue obter o total de $ {}'.format(p, resultado))


