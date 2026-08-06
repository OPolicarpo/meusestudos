'''crie um programa que tenha uma TUPLA unica com nomes de produtos e seus respectivos preços na sequencia
no final mostre uma listagem de precos organizando dados em forma tabular'''
print('-'*40)
print('Listagem de Preços'.center(40))
print('-'*40)
listagem= ('Lapis', 1.75, 'Borracha', 2.00, 'Caderno', 15.00,
            'bolsinha', 6.00, 'Caneta', 3.00, 'mochila', 79.90, 'livro', 49.90)
for pos in range(0, len(listagem)):
        if pos %2==0:
            print(f'{listagem[pos]:.<30}', end='')
        else:
            print(f'R$ {listagem[pos]:>7.2f}')


'''print(f'{listagem[0]:.<30}{listagem[1]}')
print(f'{listagem[2]:.<30}{listagem[3]}')
print(f'{listagem[4]:.<30}{listagem[5]}')
print(f'{listagem[6]:.<30}{listagem[7]}')
print(f'{listagem[8]:.<30}{listagem[9]}')
print(f'{listagem[10]:.<30}{listagem[11]}')
print(f'{listagem[12]:.<30}{listagem[13]}')'''
