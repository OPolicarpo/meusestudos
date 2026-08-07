'''faça um programa que ajude um jogador da mega sena criar palpites.
o programa vai te perguntar quantos jogos serao gerados e vai sortear 6 numeros entre 1 e 60 para cada jogo
cadastrando tudo em lista composta'''
# 1Q - Quais são os dados de entrada necessários?
# quantos jogos o usuario quer fazer
#
#
# 2Q - O que devo fazer com esses dados?
#vai gerar uma lista de 6 numeros pra cada jogo
#
#
# 3Q - Quais são as restrições deste problema?
#
#
#
# 4Q - Qual é o resultado esperado?
#mostrar em linhas separadas a sujestao aleartoria dos numeros gerados 
#
#
# 5Q - Qual é a sequência de passos para chegar ao resultado esperado?
#criar a lista
#entrar com a informacao
#gerar um range(info)
#exibir a aposta
from random import randint
from time import sleep

cont = int(input('quantos jogos voce quer que eu sorteie ?'))
for c in range(cont):
    jogo = [randint(0,60), randint(0,60), randint(0,60),
             randint(0,60), randint(0,60), randint(0,60), ]
    sleep(0.8)
    print(f'Jogo {c}: {jogo}')

    


