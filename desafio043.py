'''desenvolva uma logica que leia o peso e altura de uma pessoa, calcule o seu imc e mostre o seu status de acordo com a tabela abaixo
abaixo de 18.5 : abaixo do peso, entre 18.5 a 25: peso ideal 15 ate 30: sobrepeso, de 30 a 40 obesidade, acima de 40 obesidade morbida'''
peso= float(input('Qual e seu peso: '))
altura = float(input('Qual e sua altura: '))
imc = peso / (altura**2)
if imc <18.5:
    print('Voce esta abaixo do peso')
elif imc < 25:
    print('Voce esta no seu peso ideal')
elif imc <30:
    print('Voce esta com sobrepeso')
elif imc<40:
    print('Voce esta obeso')
else:
    print('Voce esta com obesidade morbida')
