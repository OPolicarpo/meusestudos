'''Crie um programa que leia varios valores interos pelo teclado, no final da execucao, mostre a media entre todos os valores e qual foi o maior e o menor valor lido.
o programa deve perguntar ao usuario se ele quer ou nao consitinuar a digitar valores '''
maior = 0
menor = 0 
cond = 0
soma = 0
cont = 0
mod = True
while cond != 'N':
    n = int(input('Digite um numero : '))
    cond = input(' Deseja continuar? [S] / [N]: ').upper()
    soma = soma + n
    cont = cont + 1
    if mod:
        maior = n
        menor = n
        mod = False
    if n > maior:
         maior = n
    if n < menor:
        menor = n
print (' O maior numero e {}'.format(maior))
print (' O menor numero e {}'.format(menor))    
media = soma / cont
print (' A media deles e {} '.format(media))

