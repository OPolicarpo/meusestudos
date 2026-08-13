'''crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatorioa
guarde os resultados no dicionario e no final
coloque o dicionario em ordem sabendo que o vencedor tirou o maior numero no dado.''' 
from random import randint
from time import sleep
jogadores = {}
jogo = []
rank = {}
maior = 0

for c in range(0,4):
    jogadores['nome'] = str(input('Digite seu nome: '))
    print('jogando os dados')
    sleep(0.3)
    jogadores['dados'] = randint(1,6)
    print(jogadores['dados'])
    jogo.append(jogadores.copy())
for jogadores in jogo:
    if jogadores['dados'] > maior:
        maior = jogadores['dados']
        rank.append(jogadores.copy())
print(rank)

print(jogador_ordenado)
print(max(jogo['dados']))

