'''Crie um programa que leia dois valores e motre um menu na tela:
[1] somar [2] multiplicar [3] maior / novos numeros / sair do programa
seu programa devera realizar a operacao solicitada em casa caso'''
n1 = int(input('Digite um numero: '))
n2 = int(input ('Digite outro numero: '))
r = 0
print('[1] Somar')
print('[2] Multiplicar')
print('[3] Maior')
print('[4] Novo numero')
print('[5] Sair')
escolha = int(input('Escolha uma opção: '))
while escolha != 5:
    if escolha == 1:
        r = n1 + n2
        print('A soma dos 2 e {}'.format(r))
    if escolha == 2:
        r = n1 * n2
        print('A multiplicacao deles e {}'.format(r))
    if escolha == 3:
        if n1 > n2:
            print('O maior numero e {}'.format(n1))
        elif n2 > n1:
            print('O maior numero e {}'.format(n2))
    if escolha == 4:
        n1 = int(input('Digite um numero: '))
        n2 = int(input ('Digite outro numero: '))
    r = 0
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novo numero')
    print('[5] Sair')
    escolha = int(input('Escolha uma opção: '))
print('Fim do programa')
        


