'''Crie um programa que leia VARIOS NUMEROS inteiros. o programa so vai parar 
quando o usuario digitar 999 que e a condicao de parada. no final mostre quantos numeros foram digitados
e qual foi a osma deles desconsiderando o flag'''
maior = menor = 0
cont = 0
soma = 0
comparar = True
while True:
    n = int(input(' Digite um valor: '))
    if n == 999:
        break
    soma += n
    cont += 1

print(f'a soma foi {soma}')
print(f'{cont}n. foram digitados')