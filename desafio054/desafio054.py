'''crie um programa que leia o ano de nascimento de 7 pessoas. no final mostre quantos ainda nao atingiram a maioridade e quantas ja sao maiores'''
menor = 0
maior = 0
atual = 2026
idade = 0

for c in range(0,7):
    ano = int(input('Digite sua data de nascimento: '))
    idade = atual - ano
    if idade <18:
        menor = menor + 1 
    else:
     maior = maior + 1
print('{} sao menores de idade e {} sao maiores'.format(menor, maior))