'''Escreva um programa que leia dois numeros inteiros e compara mostrando na tela uma mensagem
o primeiro valor e maior
o segundo valor e maior
nao existe valor maior, os dois sao iguais'''
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
if n1>n2:
    print('O valor {} e maior que o {}'.format(n1,n2))
elif n2>n1:
    print(' O valor {} e maior que o {}'.format(n2,n1))
elif n1==n2:
    print(' O valor {} e igual ao {} nao teve numero maior'.format(n1,n2))
