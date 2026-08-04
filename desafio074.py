'''crie um programa que vai gerar 5 numeros aleatorios e colocar em 1 tupla.
depois disso mostre a listagem de numeros gerados e infique o menor e o maior valor que estao na tupla'''
from random import randint
n = ( randint(0,20), randint(0,20), randint(0,20), randint(0,20), randint(0,20),)
print(n)
print(f'O maior valor e {max(n)}')
print(f'O menor valor e {min(n)}')