'''faca um programa que leia um numero qualquer e mostre seu fatorial'''
n = int(input('Digite um numero: '))
fator = 1
c = n

while c > 0:
    fator = fator *c
    c = c - 1

print('O fator de {} e igual a {}'.format(n, fator))