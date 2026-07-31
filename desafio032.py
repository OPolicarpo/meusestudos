#faca um programa que leia um ano qualquer e mostre se ele e bissexto
from datetime import date
ano= int(input('Digite o ano:'))
if ano == 0:
        ano = date.today().year
if ano%4==0 and ano % 100 !=0 or ano % 400 ==0:
    print(' o ano {} e bisexto!'.format(ano))
else:
    print('o ano {} nao e bixesto!'.format(ano))