'''crie um programa que tenha a funcao LEIAINT(), que vai funcionar
de formacao semelhante a funcao input do PYTHON, so que fazendo
    validacao para aceitar um valor numerico
    ex : n=leiaint('Digite um n')'''

def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('Erro! Digite um numero inteiro valido.')
        if ok:
            break
    return valor



n = leiaint(' Digite um numero: ')
print(f'Voce avabou de digitar o numero {n}')