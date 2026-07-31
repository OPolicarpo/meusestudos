#desenvolva um programa que leia o comprimento de 3 retas e diga ao usuario se elas formam um triangulo
n1= int(input('Digite o primeiro angulo: '))
n2= int(input('Digite o segundo angulo: '))
n3= int(input('Digite o terceiro angulo: '))
if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
    print('Pode ser formato um triangulo')
else:
    print('Nao pode formar um triangulo ')
