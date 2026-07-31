#aula12 sobre elif e else e if
nome = str(input('qual e seu nome? '))
if nome == 'Policarpo':
    print('Que nome bonito')
elif nome == 'Pedro' or nome== 'Maria' or nome== 'Paulo':
    print('Seu nnome e bem popular no Brasil')
else:
    print('Seu nome e bem normal')

print('Tenha um bom dia, {} !!'.format(nome))