'''Escreva um programa que leia um numero N inteiro e mostre na tela os primeiros elementos de uma sequencia de fibonacci'''

t1 = 0
t2 = 1
t3 = 0
cont = 2
n = int(input('Digite um numero: '))
print (t1)
print (t2)
while cont < n:
    t3 =t1 + t2
    cont = cont + 1
    t1= t2
    t2= t3
    print(t3)