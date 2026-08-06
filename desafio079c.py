'''crie um programa onde o usuario possa digitar varios valores numericos
e cadastre em uma lista. caso o numero ja existala dentro, ele nao sera adicionado. 
no final serao exibidos todos os valores unicos digitados em ordem crescente'''
numeros=list()
while True:
    n = int(input("Digite um valor: "))
    if n not in numeros:
        numeros.append(n)
        print('Valor adioconado com sucesso!')
    else: 
        print('Valor duplicado, nao sera adicionado!')

    r = str(input('Quer continuar? [S/N]'))
    if r in 'Nn':
        break
print('-='*30)
numeros.sort()
print(f'Voce digitou os valores {numeros}')