#faca um programa que leia o comprimento do cateto oporto e do adjacente e um triangulo retangulo, calcule e mostre o comprimento da hipotenusa
from math import hypot
c1 = float(input('Digite o cateto 1 :'))
c2 = float(input('Digite o cateto 2: '))
h= hypot(c1, c2)
print('A hiputenusa desse triangulo é {}'.format(h))
