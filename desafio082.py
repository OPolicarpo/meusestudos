'''crie um programa que vai ler varios numeros e colocar em 1 lista
depois disso crie duas listas
a com pares
b com impares
no final mostre as 3'''
valor = []
par = []
impar = []
while True:
    valor.append(int(input('Digite um Valor = ')))
    cond = input('Deseja continuar? S / N = ').upper()
    while cond != 'S' and cond != 'N':
        print('Opçao invalida, digite novamente!')
        valor.append(int(input('Digite um Valor = ')))
    if cond == 'N':
        break
for num in valor:
    if num %2==0:
        par.append(num)
    if num %2!= 0:
       impar.append(num)
print('-='*30)
print(f'A lista completa é = {valor}')
print(f'A lista de impares é = {par}')
print(f'A lista  de impar é = {impar} ')