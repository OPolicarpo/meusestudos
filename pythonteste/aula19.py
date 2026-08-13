''' pessoas = {'nome': ' Policarpo', 'sexo': 'M' , 'idade' : 22  }
pessoas['peso'] = 110
for k, v in pessoas.items():
    print(f'{k} = {v}')''' 
''' brasil=[]
estado1 = {'uf': ' Rio de janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'Sao Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(estado2)
print()
print(estado1)
print()
print(brasil)
print()
print(brasil[0])
print()
print(brasil[0]['uf'])'''

estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input(' Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
    #nao posso esquecer disso pra copiar pra dentro do dicionario, e diferente das listas
for e in brasil:
    for k,v in e.items():
       # print(f'o campo {k} tem valor {v}')
       print(v, end='')
    print()