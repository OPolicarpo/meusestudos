'''crie um programa que leia a idade e o sexo de varias pessoas. a cada pessoa cadastrada o programa
devera perguntar se o usuario quer continuar e no final mostre
quantas pessoas tem 18 anos  / quantos homens foram cadastrados / quantas mulheres tem 20 anos'''
midade = 0
hcad = 0
menor= 0
while True:
    sexo = input('Qual seu sexo H/M: ').upper()
    i = int(input('Sua idade: '))
    dec = input('quer continuar? S/ N ').upper()
    if i>18:
        midade+=1
    if sexo == 'H':
        hcad += 1
    if sexo =='M' and i <20:
        menor+=1
    if dec == 'N':
        break
print(f'{midade} tem 18 anos')
print (f'{hcad} homens foram cadastrados')
print (f'.{menor} mulheres tem menos de 20 anos')