'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

-Se ele ainda vai se alistar ao serviço militar.
-Se é a hora de se alistar.
-Se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

from datetime import date

sexo = str(input('Digite [M] para sexo Masculino\nDigite [F] para sexo Feminino: '))
sexo = sexo.upper()

if sexo == 'F':
    print('Você não precisa se alistar Mocinha! ')

else:
    ano_nasc = int(input('Digite o seu anode nascimento: '))

    ano_atual = date.today().year
    ano_alistamento = ano_atual - ano_nasc #se alista com 18 anos

    print('Voce tem {} anos!'.format(ano_alistamento))

    if ano_alistamento < 18: #verifica se o soldado ainda n fez 18 anos e calcula quantos anos falta para o alistamento
        print('Você ainda esta novo para se alistar! ')

        tempo_passou = 18 - ano_alistamento
        print('Ainda falta {} anos, fique tranquilo! '.format(tempo_passou))

    elif ano_alistamento == 18:  #verifica se o soldado tem 18 anos, se tiver precisa se alistar
        print('Está na hora do seu Alistamento!')

    elif ano_alistamento > 18: #verifica se o soldado tem mais de 18 anos,se sim ele precisa se alistar e calcula quanto tempo passou do alistamento
        print('Jã passou da hora de você se alistar!')

        tempo_passou =  ano_alistamento - 18
        print('Você deveria ter se alistado a {} anos, vá ao posto de alistamento mais proximo !'.format(tempo_passou))

