'''Escreva um programa que leia um numero inteiro qualquer e peca o usuario pra escolher 
qual sera a base de conversao 1- numerica 2 octal 3 hexadecimal
'''
n= int(input('Escreva um numero para conversao: '))
print('[1] Para converter para binario')
print('[2] Para converter para ectal')
print('[3] Para converter para hexadecimal')
op= int(input('\033[1;33;44m Escolha uma opcao: \033[m'))
if op== 1:
    print(' \033[1;31;34m O seu numero convertido para binario e {} \033[m '.format(bin(n)))
elif op== 2:
    print('\033[1;32m O seu numero convertido para octal e {} \033[m'.format(oct(n)))
elif op== 3:
    print(' \033[1;33m O seu numero convertido para hexadecimal e {} \033[m'.format(hex(n)))
else:
    print(' opcao invalida')