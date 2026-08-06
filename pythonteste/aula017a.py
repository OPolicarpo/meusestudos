valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))

for c,v in enumerate(valores):
    print(f'na posiçao {c} encontrei o valor {v}')
print('Cheguei no final da minha lista')
