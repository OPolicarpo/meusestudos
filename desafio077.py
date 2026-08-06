'''crie um programa que tenha uma tupla com varias palavras
depois disso voce dve mostrar para cada palabra quais sao as suas vogais'''
lista= ('arroz', 'feijao', 'batata', 'macarrao')
vogai = 'aeiou'
for p in lista:
    print ( f'\nNa palavra {p.upper()} temos ', end='')
    for lista in p:
        if lista.lower() in 'aeiou':
            print(lista, end=' ' )