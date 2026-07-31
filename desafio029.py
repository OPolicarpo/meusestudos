#escreva um programa que leia a velocidade de um carro, 
# se ele ultrapassar 80kmh, mosttre uma mensagem dizendo que ele foi multado
# a multa vai custar 7 por cada km acima do limite
import emoji

print(" Vrummmmmmmm🚀🚀")
km= float(input('Qual velocidade voce foi flagrado? '))
lv = 80
multa = ((km-lv)*(7.00))
if km>lv:
    print('Voce ultrapassou o limite de velicidade, sua multa foi de {}'.format(multa))
else:
    print('Uffa, voce estava abaixo do limit de velocidade')