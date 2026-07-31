#faca um programa que leia um numero inteiro qualquer e mostre a sua tabuada
n = int(input('digite um numero para apresentacao da tabuada: '))
for i in range(1, 11):
    r = n * i
    print('{} x {} = {}'.format(n,i,r))
