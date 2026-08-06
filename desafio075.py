'''desenvolva um programa que leia 4 VALORES pelo teclado e guarde-os em uma tupla. no final mostre
a- quantas vezes apareceu o 9
b- em que posicao foi digitado o primeiro valor 3
c- quais foram os numeros pares'''
n= ( 
    int(input('Digite o 1o. numero: ')),
   int(input('Digite o 2o. numero: ')),
   int(input('Digite o 3o. numero: ')),
   int(input('Digite o 4o. numero: '))
   )   
if 9 in n:
    print(f'A- O 9 apareceu {n.count(9)} vezes')
else: 
    print('O valor 9 nao apareceu nenhuza vez')   
if 3 in n:
    print (f'B- O 3 apareceu {n.index(3)+1} posicao')
else: print('O numero 3 nao apareceu em nenhuma posiçao')
for numero in n:
    if numero %2 == 0:
       
        print(f'C- Os numeros pares são {numero}')

