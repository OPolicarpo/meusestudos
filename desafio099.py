''' faca uma funcao que chamada MAIOR(), que receba varios parametros
com valores inteiros.
seu programa tem que analizar os valores e dizer qual deles e maior.'''
#vamos usar parametros variaveis e desempacotamento
from time import(sleep)

def maior(* num):
    cont = maior = 0
    print(' Analisando os valres passados...')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0 :
            maior = valor
        else:
            if valor > maior:
                maior=valor
        cont+=1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor foi {maior}')


#programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()