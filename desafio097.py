'''faca um programa que tenha uma funcao chamada escreva()
que receba um testo qualquer como parametro e mostre
uma mensagem com ramanho adaptavel.'''

def titulo(txt):
    print('='*(len(txt) + 2))
    print(txt)
    print('='*(len(txt) + 2))

    
    
txt = str(input('Digite um titulo: '))
titulo(txt)
