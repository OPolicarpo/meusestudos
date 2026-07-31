'''refaca o desafio 35 dos triangulos arescentando o recurso de mostrar o tipo de triangulo sera formado
equilatero - todos lados iguias, isoceles - dois lados iguais - escaleno todos os lados diferentes'''

n1= int(input('Digite o primeiro angulo: '))
n2= int(input('Digite o segundo angulo: '))
n3= int(input('Digite o terceiro angulo: '))
if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
    print('Pode ser formato um triangulo')
    if n1 == n2 and n1 == n3 and n2 == n3:
        print('O seu triangulo e EQUILÁTERO')
    elif n1 == n2 or  n1 == n3 or n2==n3: 
        print('O seu triangulo e ISÓCELES')
    elif n1 != n2 and n1 != n3 and n2 != n3:
        print('O seu triangulo é ESCALENO')     
else:
    print('Nao pode formar um triangulo ')