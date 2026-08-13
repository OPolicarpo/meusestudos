'''crie um programa que gerencie o aproveitamento de u jogador de futebol.
o programa vai ler o nume do jogador e quantas partidas ele jogou.
depois vai ler a quandidade de gols feitos em cada partida.
no final tudo isso sera guardado em 1 dicionario
incluindo o total de gols feitos durante o campeonato'''
jogador= {}
est=[]

jogador['nome'] = str(input("Nome do Jogador: "))
partidas = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
for c in range(partidas):
    gols = int(input(f'Quantos gols na partida {c} : '))
    est.append(gols)
jogador['gols'] = est
jogador['total'] = sum(est)

print('-='*40)
print()
print (jogador)
print()
print('-='*40)
print(f'O campo nome tem o valor {jogador['nome']}')
print(f'O campo Gols marcados tem o valor {jogador['gols']}')
print(f'O campo total de gols tem o valor {jogador['total']}')
print()
for partidas,gols in enumerate(jogador['gols']) :
    print(f'Na partida {partidas}, fez {gols}')
print()
print(f'Foi um total de {jogador['total']} gols.')