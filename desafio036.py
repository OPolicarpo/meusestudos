'''Escrevam um programa para aprovar emprestimo bancario para comprar uma casa.
o programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
CALCULE O VALOR DA PRESTACAO MENSAL, SABEM QUE ELA NAO PODE EXEDER 30% DO SALARIO OU ENTAO O EMPRESTIMO SERA NEGADO'''
casa= float(input('Digite o valor da casa que quer comprar: '))
salario= float(input('Digite o valor do seu salario: '))
meses = float(input('Quantos anos vai pagar a casa: '))
meses = meses *12
parcela= salario/100*30

if  casa/meses < parcela:
    
    print('\033[32m Seu emprestimo esta aprovado\033[m')
else:
    print('\033[31m seu emprestimo nao foi aprovado\033[m')
