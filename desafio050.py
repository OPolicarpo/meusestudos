''' Desenvolva um programa que leia seis numeros inteiros e mostr a  apenas a soma dos que forem pares, se o valor for impar desconsidere'''

soma = 0
for c in range (0,6):
    valor = int(input('Digite um numero: '))
    if valor % 2 == 0:
        soma = soma + valor
print('A soma dos valores pares e {}'.format(soma))