'''crie uma TUPLA com os 20 primeiros colocados da tabela do brasileirao, na ordem de colocacao, depois mostre
a- apenas os 5 primeiros colocados
b- os ultimos 4 colocados
c- uma lista com os times em ordem alfabetica
d- em que posicao esta o vasco'''
times = ('Palmeiras', 'Flamengo', 'Athletico-PR', 'Fluminense', 'Bahia',
          'Bragantino', 'Cruzeiro', 'Botafogo', 'Corinthians', 'Atlético-MG',
            'Coritiba', 'São Paulo', 'Vitória', 'Mirassol', 'Santos', 'Internacional', 
            'Grêmio', 'Vasco', 'Remo', 'Chapecoense')
print(f'A- G5 = {times[0:5]}')
print('-='*50)
print(f'B- Z4 = {times[-4:]}')
print('-='*50)
print(sorted(times))
print('-='*50)
print(f'Times em ordem alfabetica : {sorted(times)}')
print(f'Vasco esta em {times.index('Vasco')+1} lugar')
