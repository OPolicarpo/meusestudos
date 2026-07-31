from random import randint
from time import sleep
pc = randint(0,10)
user = 0
while pc != user:
    user= int(input('Adivinhe o numero de 0 a 10 que o pc pensou: '))
    if pc != user:
        print ('O numero do pc {} e o seu {}, voce perdeu'.format(pc,user))
    
print('O numero do pc foi {} e o seu {}, voce ganhou'.format(pc,user))