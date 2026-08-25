'''reescreva a funcao LEIAINT() do desafio 104, incluindo agora a possibilidade 
digitacao de um numero de tipo invalido.
aproveite e crie tbm uma funcao leiaflorat() com a mesma funcionalidade'''


try :
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

    
    def leiafloat(n):
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
o = leiafloat ('Digite um Real: ')
print(f'Voce avabou de digitar o numero {n}')