from random import randint
from time import sleep
computador= randint(0,5)
jogador = int(input('Em que numero pensei?'))
print('Processando...')
sleep(3)
if computador==jogador:
    print('Parabens, voce adivinhou o numero do computador')
else:
    print('Ganheiro, eu pensei no numero {} e nao no numero {}'.format(computador,jogador))