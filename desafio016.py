#crie um programa que mostre um numero real qualquer pelo teclado e mostre a sua tela a porcao inteira :
#ex digite um numero: 6.127, o numero 6.127 tem a parte inteira 6
from math import trunc
n = float(input('Digite um numero: '))
print('o numero {} tem a parte inteira {}'.format(n, trunc(n)))