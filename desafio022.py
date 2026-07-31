#crie um programa que leia o nome completo de uma pessoa e mostre
#nome com todas as letras maiusculas
#nome com todos minusculos
#quantas letras ao todo sem considerar o espaco
#quantas letras tem o primeiro nome
frase = input(' Qual e seu nome? ')
print(frase.lower())
print(frase.upper())
j = (frase.replace(' ',''))
print(len(j))
p1= (frase.find(' '))
print(frase[:p1])

