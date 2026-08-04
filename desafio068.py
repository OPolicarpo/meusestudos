'''faca um programa que jogue impar ou par com o computador. 
o jogo sera interrompido quando ele perder, mostrando o total de 
vitorias consecutivas que ele conquistou'''
print(' PAR OU IMPAR')
from random import randint
vc= 0
while  True:
    player = (int(input('Digite um numero de 0 a 5: ')))
    op = input (' Escolha par ou impar ').upper()
    pc = randint (0,5)
    soma = player + pc
    if soma %2==0:
        r = 'PAR'
    elif soma %2 ==1:
        r = 'IMPAR'
    print(f'vc escolheu {player} e o pc {pc} e a soma foi {soma} e deu {r}')
    if soma == r:
        vc+=1
        print(' Voce venceu ')
    else:
        break
print(f'Voce perdeu, mas teve {vc}')
