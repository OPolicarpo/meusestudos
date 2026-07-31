''' a confederacao nacional de natacao precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade
ate 9 mirim, ate 14 infantil, ate 19 junior, ate 20 senior, acima master'''

idade = int(input('Insira sua idade:'))
if idade  < 9:
    print(' Voce e um atleta MIRIM!')
elif idade < 14:
    print('Voce é um atleta INFANTIL')
elif idade < 17:
    print('Voce e um atleta JUNIOR')
elif idade < 20:
    print('Voce e um atleta SENIOR')
else:
    print('Voce e um atleta MASTER')
