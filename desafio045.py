'''Crie um programa que faca o computador jogar jokenpo com voce'''
from random import randint
import emoji
print('==== Jokenpo ====')
print ('[1] ✊')
print ('[2] 🖐')
print('[3] ✌')

print('==== Jokenpo ====')

op= int(input('Escolha sua opcao'))
pc= randint(1,3)
if op == 1 and pc == 3:
    print('O pc escolheu ✌ e voce ✊, VOCE venceu!')
elif op == 1 and pc == 2:
    print('O PC escolheu 🖐 e voce ✊, COMPUTADOR venceu ')
elif op == 2 and pc == 1:
    print('O PC escolheu ✊ e voce 🖐, VOCE venceu')
elif op == 2 and pc == 3:
    print('O PC escolheu ✌ e voce 🖐, COMPUTADOR venceu')
elif op == 3 and pc == 1:
    print('O PC escolheu ✊ e voce ✌, COMPUTADOR venceu')
elif op == 3 and pc == 2:
    print('O PC escolheu 🖐 e voce ✌, VOCE venceu ')
elif op==pc:
    print('Joguem novamente')
else:
    print('opcao invalida, tente novamente')

