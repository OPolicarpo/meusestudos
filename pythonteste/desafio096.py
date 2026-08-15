''' faca um programa que tenha uma funcao chamada area(), que receba as dimencoes
de um terreno retangular(largura e comprimento) e mostre a area do terreno.'''


def area(a,b):
    s= a * b
    print(f'A area de um terreno com {a}x{b} e de {s}m2')

#programa principal
print('Controle dos terrenos ')
print('='*40)
a = float(input('Largura (m): '))
b = float(input('Comprimento (m): '))
area(a , b)