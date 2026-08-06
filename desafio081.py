'''crie um programa que vai ler varios numeros e colocar numa lista
depois disso, mostre
a- quantos numeros foram digitados
b a lista de valores ordenada de forma decrescente
c se o valor 5 foi digitado na lista'''
numeros = []
cont= 0

while True:
    numeros.append(int(input('Digite um numero: ')))
    cont +=1
 
    cond= input('Deseja continuar: S / N ').upper()
    if cond != 'S' and cond != 'N':
         print('Opção invalida') 
    if cond == 'N' :
        break
    
print(f'{cont} numeros foram digitados na lista')
numeros.sort(reverse=True)
print(f'A lista de forma ordenada decrescente é {numeros}')
if 5 in numeros:
    print('O numero 5 foi digitado')
else: 
    print('O numero 5 nao foi digitado')




