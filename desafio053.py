'''crie um programa que leia uma frase e diga se ela e um palidromo, desconsiderando os espacos'''
frase = input('Digite uma frase qualquer:')
frase = frase.replace(' ', '')
frase = frase.lower()
inver = frase[::-1]
if frase == inver:
    print('A frase e Palidromo')
else: 
    print('A frase nao e Palidromo')
