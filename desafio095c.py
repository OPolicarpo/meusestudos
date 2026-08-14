time = list()
jogador = dict()
partidas = list()
while True:
    jogador['nome']= str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'      Quantos gols na partida {c}? ')))    
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    resp = str(input('Continua? [s/n]: ')).upper()[0]
    time.append(jogador.copy())
    while True:
        if resp in 'SN':
            break
        print('ERRO, RESPONDA APENAS COM S OU N')
    if resp == 'N':
        break
print('-='*30)
print(' cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}',end='')
print('-='*30)

for k , v in enumerate(time):
    print(f' {k:>4}', end='')
    for d in v.values():
        print(f' {str(d):<15}', end='')
    print()
print('-='*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro, nao esxite jogador com codigo {busca}')
    else:
        print(f' -- Levantamento do jogador {time[busca]['nome']}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i+1} fez {g} gols')
'''print('_-'*30)
print(f' O jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas')
for i, v in enumerate(jogador['gols']):
    print(f'     => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador['total']} gols ')'''
