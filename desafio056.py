'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. no final mostre
a media de idade do grupo / nome do homem mais velho, quantas mulheres tem menos de 20 anos'''
c = 0
soma_idade = 0
mulhermenor = 0
hmaior = 0
vhomem= ''
mediai= 0
for c in range (4):
    nome = input('Digite seu nome: ')
    idade = int(input('Quantos anos: '))
    sexo = input('Qual sexo [M] ou [H]: ').lower()
    idade = idade
    soma_idade = soma_idade + idade
    if sexo == 'm':
        if idade <20:
            mulhermenor = mulhermenor + 1
    if sexo == 'h' and idade > hmaior:
        hmaior = idade
        vhomem = nome
    
media = soma_idade / 4
print( 'A Media de idade e {}'.format(media))
print('{} Mulheres menores '.format(mulhermenor))
print('O {} e o homem mais velhor com {} anos'.format(vhomem, hmaior))