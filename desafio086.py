'''crie um programa que crie uma matris de dimensao 3x3 e
preencha com valores lidos pelo teclado
no final mostre a matris na tela com a formatacao correta'''
matris = []
linha_atual = []

for linha in range(0,3):
    linha_atual = []
    for coluna in range(0,3):
        valor = int(input(f'Digite um palor para {linha,coluna}'))
        linha_atual.append(valor)
    matris.append(linha_atual)
    linha_atual.clear
print(f'[ {matris[0][0]} ]  [ {matris[0][1]} ]  [ {matris[0][2]} ]') 
print(f'[ {matris[1][0]} ]  [ {matris[1][1]} ]  [ {matris[1][2]} ]')
print(f'[ {matris[2][0]} ]  [ {matris[2][1]} ]  [ {matris[2][2]} ]')