'''faça um programa que leia o nome e peso de varias pessoas, 
guardando tudo numa lista. no final mostre
a - quantas pessoas foram cadastradas
b - uma lista com as pessoas mais pesadas
c - uma listagem com as pessoas mais leves.'''
cad= []
lista = []
qnt = 0

print('-='*30)
print('Cadastro de cliente')
print('-='*30)
while True:
    lista.append(str(input('Digite o nome: ')))
    qnt +=1
    lista.append(int(input('Digite o peso: ')))
    
    cad.append(lista[:])
    lista.clear()
    cond= input('Deseja continuar? [S/N]').upper()
    if cond == 'N':
        break
        print('Fim de cadastro')
pesado = cad[0][1]
leve = cad[0][1]
print(f'Foram cadastradas {qnt} pessoas')
for i in cad:
    if i[1] > pesado :
        pesado = i[1]
    if i[1] < leve:
        leve = i[1]
for i in cad:
    if i[1] == pesado:
        print(f'O mais pesado foi {i[0]} com {i[1]} kg')
    if i[1] == leve:
        print(f'O mais leve foi {i[0]} com {i[1]} kg')
        




