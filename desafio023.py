#faca um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados
#ex numero:1834 / r / unidade 4, dezena 3, centena 8 e milhar 1
n1 = input(' Digite um numerode 0 a 9999: ').zfill(4)
print('unidade: ', n1[3])
print('dezena: ', n1[2])
print('centena: ', n1[1])
print('milhar: ', n1[0])