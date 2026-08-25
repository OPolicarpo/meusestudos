'''faca um programa que tanha uma funcao chamada CONTADOR().
que receba 3 parametros: INICIO, FIM E PASSO  e realize a contagem.
seu programa tem que realizar 3 contagens atraves da funcao criaca
a - de 1 ate 10, de 1 em 1
b - de 10 ate 0, de 2 em 2
c - uma contagem personalizada'''

from time import sleep
def contador(a, b, c):
    print('=-'*30)
    print(f'Contagem de {a} ate {b} de {c} em {c}')
    for cont in range(a,b,c):
        print(cont, end='', flush=True)
        sleep(0.5)
        print()
        
    print('-='*30)
    
    print()
contador(10, 0, -2)
contador(0, 11, 1)
while True:
    a = int(input('Inicio: '))
    b = int(input('Fim: '))
    c = int(input('passo: '))
    if c == 0:
        c=1
        if a > b:
            c = -(c)
    contador(a, b, c)
    break




            