'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preco normal e condicao de pagamento
a vista = 10% de desconto / cartao 5% / em 2x o preco normal, 3x pra la, 20% de juros'''
valor= float(input('Digite o valor do produto: '))
print('==============================')
print('Qual a forma de pagamento?')
print('==============================')

print('[1] A vista')
print('[2] cartao 1x')
print('[3] 2x no cartao')
print('[4] 3x ou mais')

op= int(input('Digite sua opcao: '))

if op== 1:
    valor = valor-(valor/100*10)
    print('O total a pagar e {:.2f}'.format(valor))
elif op==2:
    valor = valor - (valor/100*5)
    print('O valor a pagar e {:.2f}'.format(valor))
elif op==3:
    valor = valor/2
    print('Voce vai pagar 2 parcelas de {}'.format(valor))
elif op==4:
    x= int(input('Digite a quantidade de parcela: '))
    valor = (valor + (valor/100*20))/ x
    print('Voce pagara {} parcelas de {}'.format(x, valor))
else:
    print('opcao invalida')