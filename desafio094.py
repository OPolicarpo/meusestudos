'''crie um programa que leia NOME, SEXO E IDADE  de varias pessoas
guardando os dados de cada pessoa em um dicionario e todos os dicionrios
em uma lista. no final mostre:
a- quantas pessoas foram cadastradas
b- a media de idade do grupo
c- uma lista com todas as mulheres
d- uma lista com todos as pessoas com idade acima da media.'''
cad = {}
qnt = 0
pessoas = []
while True:
    cad['nome']= str(input('Nome: '))
    cad['idade'] = float(input('idade: '))
    cad['sexo'] = str(input('Sexo: [M/f]')).upper()
    cond = input('deseja continuar? [s/n]').upper()
    qnt += 1
    pessoas.append(cad.copy())
    if cond=='N':
        break
soma = 0
for pessoa in pessoas:
    soma += pessoa['idade']
print(f'A media da idade e de {soma/qnt}')
print(f'O grupo tem {qnt} pessoas')

for pessoa in pessoas:
    if pessoa['sexo']== 'F':
        print(f'sexo feminino {pessoa['nome']}', end='')
        print()
media = soma / qnt
for pessoa in pessoas:
    if pessoa['idade'] > media:
        print(f'lista de pessoas que estao acima da media {pessoa['nome']}')


print('<< ENCERRADO >>')
