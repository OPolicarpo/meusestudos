'''Crie um programa onde o usuari possa digitar 7 valores numericos e
cadastreos em uma lista unica que mantenha separado os valores pares e impares.
no finl mostre os valores pares e impares em ordem crescente'''

# vou declarar os nomes de cada lista
pares= []
impares = []
for i in range(1,8):
    valor = int(input(f'Digite o {i}o. valor: '))
    if valor %2==0:
        pares.append(valor)
    elif valor %2 ==1:
        impares.append(valor)
pares.sort()
print(f'Os numeros pares são {pares}')
impares.sort()
print(f'Os numeros impares são {impares}')
