#faca um programa que leia a largura e a altura de uma parede em petros, calcule sua area e a quantidade de tinta necessaria para pintala, sabendo que cada litro de tinta pinta uma area de 2mquadrados.
a=float(input('digite a altura da parede: '))
l=float(input('digite a largura da parede: '))
m= a*l
q= m/2
print(' para pintar {}** de parede e necessario {} litros de tinta'.format(m,q))