'''valores=[]
valores.append(5)
valores.append(9)
valores.append(4)'''
valores=list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))

for c,v in enumerate(valores):
    print(f'na posicao {c} encontrei o valor {v}...', )
print('Cheguei ao final da lista')