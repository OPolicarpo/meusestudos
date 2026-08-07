'''aprimore o desafio anterior mostrando no final
a- a soma de todos os valores pares digitados
b- a soma de dos valores da terceira coluna
c- o maior valor da segunda linha'''

matris = []
linha_atual = []
par = 0
terceira = 0
maior = 0

for linha in range(0,3):
    linha_atual = []
    for coluna in range(0,3):
        valor = int(input(f'Digite um palor para {linha,coluna}'))
        linha_atual.append(valor)
       
        if valor %2 ==0 :
            par = valor + par
        if coluna == 2:
            terceira+= valor
        if linha == 1 and valor > maior:
            maior = valor
    matris.append(linha_atual)
    linha_atual.clear


print(f'[ {matris[0][0]} ]  [ {matris[0][1]} ]  [ {matris[0][2]} ]') 
print(f'[ {matris[1][0]} ]  [ {matris[1][1]} ]  [ {matris[1][2]} ]')
print(f'[ {matris[2][0]} ]  [ {matris[2][1]} ]  [ {matris[2][2]} ]')
print(f'A soma dos numeros pares é : {par}')
print(f'A soma da terceira coluna e: {terceira}')
print(f'O maior numero da segunda linha e {maior}')

