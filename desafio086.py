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
print(f'\n[ {matris} ]')