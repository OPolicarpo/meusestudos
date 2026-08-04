'''Crie um programa que leia o nome e o preco de varios produtos.
o programa devera perguntar se o usuario vai continuar. no final mostra
qual e o total gasto / quantos produtos custam mais de 1000/ qual e o nome do produto mais barato'''
total = 0
custam = 0
mpreco = 0
barato = 0
nbarato = ''
mod = True
while True:
    n = input('Digite o nome do produto: ')
    preco = float(input('Digite o preco do produto: '))
    total += preco
    if preco > 1000:
        custam += 1
    if mod :
        barato = preco
        nbarato = n    
        mod = False
        if preco < barato:
            nbarato = n
    while dec != 'N' and dec != 'S':
        dec = input ('Deseja continuar S/N: ').upper() 
    if dec == 'N':  
        break
print(f'O total gasto foi {total} ')
print(f'o total de produtos acima de 1000 foram {custam} ')
print(f'O produto mais barato foi {nbarato}')
    
