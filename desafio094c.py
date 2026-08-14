'''esse eu passei aperto!
tenho tido dificuldades nessa mistua de lista com dic e tuplas kkkkkk
'''
pessoa = dict()
galera = []
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('nome: '))
    while True:
        pessoa['sexo'] = str(input('sexo [M/F]: ')).upper()[0]#[0] pega so a primeira letra
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! Por favor digite apenas M ou F.')
    pessoa['idade'] = int(input('idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True: 
        resp = str(input('continua? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('Erro! responda corretamente')
    if resp == 'N':
        break

print()
print('='*30)
print(galera)
media = soma / len(galera)
print(f'A media de idade e de {media:5.2f} anos. ')
print('As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f' {p['nome']} ', end='')
print()
print('Lista de pessoas que estao acima da media: ')
for p in galera:
    if p['idade'] >= media:
        print('    ')
        for k, v in p.items():
            print(f' {k} = {v} ', end='')
print('>> Encerrado <<')