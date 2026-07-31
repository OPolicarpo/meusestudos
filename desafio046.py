'''faca um programa que mostre na tela uma contagem regressiva de fogos de ar'''
print('-====================-')
from time import sleep

for c in range (10,0,-1):
    print('Faltam {} Segundos'.format(c))
    sleep(1)
print('\033[1;31mBOOOOOOMMMMM!!! 🎆\033[m')