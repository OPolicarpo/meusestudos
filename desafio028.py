#escreva um programa que faca o computador pensar em um numero inteiro entre 0 e 5 e peca para o usuario tentar descobrir qual foi o numero escolhido pelo computador.
#o programa devera responder na tela se o usuario perdeu ou venceu
import random 
print('============================')
print('   Acerte o numero do pc    ')
ran= random.randint(0,5)

num = int(input('Digite um numero de 0 a 5 '))
if (ran==num):
    print('seu numero foi {} e o numero do pc foi {}, Parabens voce acertou'.format(num, ran))
else:
    print('seu numero foi {} e o numero do pc foi {}, Opa, voce errou'.format(num, ran))
print('__FIM__')

import random 
print('============================')
print('   Acerte o numero do pc    ')
ran= random.randint(0,5)

num = int(input('Digite um numero de 0 a 5 '))
#if (ran==num):
print('O seu numero foi {} e o numero do pc foi {}'.format(num,ran))
print('Parabens voce acertou' if ran==num else 'Nao foi dessa vez')
 #   print('seu numero foi {} e o numero do pc foi {}, Parabens voce acertou'.format(num, ran))
#else:
 #   print('seu numero foi {} e o numero do pc foi {}, Opa, voce errou'.format(num, ran))