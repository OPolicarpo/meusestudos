'''faca um programa que leia um numoero inteiro e diga se ele e ou nao um numero primo'''

n= int(input('Digite seu numero para saber se e primo: '))
cont = 0
for c in range (1,n+1):
    if n %  c == 0:
     cont = cont + 1
if cont == 2:
        print('O numero e primo') 
else:
        print('o numero nao e primo')
    
      

        