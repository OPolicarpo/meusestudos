'''aprimore o desafio 093 para que ele funcione com varios jogadores
incluindo um sistema de visualizacao de detalhes do aproveitamento de cada jogador'''
'''adicionar while, mostrar o cod = posicao, nome, gols, total
mostrar dados do jogador referente ao codigo'''
jogador= {}
jogadores = []
est=[]
while True:
    jogadores['nome'] = str(input("Nome do Jogador: "))
    partidas = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
    for c in range(partidas):
        gols = int(input(f'Quantos gols na partida {c} : '))
        jogadores.append(gols)
    jogador['gols'] = est
    jogador['total'] = sum(est)
    cond = input('Deseja continuar? [s/n]')
    if cond in 'Nn':
        break
print('-='*40)
print()
print()
print('-='*40)

for jogo in jogador:
    print(f'{jogo}  {jogo['nome']} fez {jogo['gols']}')



'''for partidas,gols in enumerate(jogador['gols']) :
    print(f'Na partida {partidas}, fez {gols}')
print(f'Foi um total de {jogador['total']}gols.')'''