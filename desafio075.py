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
print(f'A- O 9 apareceu {n.len(9)}')