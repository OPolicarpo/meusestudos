'''faca um prorama que leia 5 valores numericos e guarde-os em uma lista
no final mostre qual foi o maior e o menor digitado e as suas respectivas posiçoes na lista'''
valores = list()
for c in range (0,5):
    valores.append(int(input('Digite um valor: ')))
    maior = max(valores)
    menor = min(valores)

print(f'O maior valor foi {maior} nas posições ', end='')
print(f'O maior valor foi {menor} nas posições ', end='')
for pos, valor in enumerate(valores):
    if valor == maior:
        print(f'{pos}... ', end='')
    if valor == menor:
        print(f'{pos}... ',end='')