'''Faca um programa que calcule a soma de todos os umeros impares que sao multiplis de trs e que se encontram no intervalor de 1/500'''
cont = 0
soma = 0
for c in range (1,501):
   if c %3 == 0 :
    soma += c
    cont += 2
print('a soma de todos os {} valores solicitados e {}'.format(cont, soma))