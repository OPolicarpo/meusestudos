#desenvolva um programa que pergunta a distancia de uma viagem em km e caldule o preco da passagem
#0,50 ate 200km e a partir de 201 0,45
km= float(input('Qual e a distancia da viagem em KM '))
if km<=200:
    km = km*0.50
    print('O valor da sua passagem e {}'.format(km))
else:
    km = km*0.45
    print(' O valor da sua passagem e {}'.format(km))
