''' Desenvola um programa que leia o primeiro termo e a razao de uma PA. no final mostre os 10 primeiros termos dessa progressao'''


termo= int(input('Digite o primeiro termo: '))
razao= int(input('Digite a razao: '))
for c in range (0,10):
    termo = termo + razao
    print(termo)       