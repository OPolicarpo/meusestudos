#faca um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente
from math import sin, cos, tan, radians
an = float(input('Digite o angulo a ser calculado: '))
rad = radians(an)
seno = sin(rad)
cose = cos(rad)
tang = tan(rad)
print('O seno e : {:.2f}'.format(seno))
print("o cosseno e :{:.2f}".format(cose))
print('A tangente e : {:.2f}'.format(tang))