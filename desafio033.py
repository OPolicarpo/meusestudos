#faca um programa ler 4 numeros e mostrar qual e o menor e qual e o maior
n1= int(input('Digite o 1o. numero: '))
n2= int(input('Digite o 2o. numero: '))
n3= int(input('Digite o 3o. numero: '))
if n1 > n2 and n1 > n3:  
    n1=n1 
    print('o numero maior foi {}'.format(n1))
elif n2 > n1 and n2 > n3:
    n2=n2
    print('O numero maior foi {}'.format(n2))
else:
    print(' o maiornumero foi {}'.format (n3))