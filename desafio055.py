'''faca um programa que leia o peso de cinco pessoas, no final mostre qual foi o meior e o menor peso lido.'''
maior = 0
menor = 0
for c in range (1,6):
    peso = int(input(' Digite o {} o. peso: '.format(c)))
    if c == 1 :
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso

print('O maior peso e {} e o menor peso e {}'.format(maior, menor))