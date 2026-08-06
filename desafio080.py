'''crie um programa onde o usuario possa digitar conco valores numericos e cadastreos em uma lista
ja na correta posiçao sem usar o sort(). no final mostre a lista ordenada na tela'''
valores = []
for c in range(0,5):
    numero = int(input(f'Digite o {c}o. numero: '))
    if c == 0 or numero > valores[-1]:
        valores.append(numero)
    else:
        pos = 0
        while pos < len(valores):
            if numero <= valores[pos]:
                valores.insert(pos, numero)
                break
            pos +=1
print(valores)



'''
for pos, valor in valores:'''
#    if valores.insert !+ valor:
