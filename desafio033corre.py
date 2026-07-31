n1= int(input('Digite o 1o. numero: '))
n2= int(input('Digite o 2o. numero: '))
n3= int(input('Digite o 3o. numero: '))
menor = n1
maior = n2
if n2<n1 and n2<n3:
    menor=n2
if n3<n1 and n3<n2:
    menor=n3
maior= n1
if  n2>n1 and n2>n3:
    maior=n2
if n3>n1 and n3>n2:
    maior=n3
print("O menor valor digitadoi foi {}".format(menor))
print('O maior valor digitado foi {}'.format(maior))