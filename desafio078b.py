valores=list()

for c in range(0,5):
    valores.append(int(input(f'Digite um valor para posição {c}: ')))
maior = max(valores)
menor = min(valores)
for pos, valor in enumerate(valores):
    if valor == maior:
        print(f'O maior valor e {maior} na posição {pos}')    
    if valor == menor:
        print(f'O menor valor e {menor} na posição {pos}')

