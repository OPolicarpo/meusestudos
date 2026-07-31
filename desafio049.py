'''refaca o desafio 009 mostrando a tabuada de um numero que o usuario escolhar, so que agora usando o laco for'''
n = int(input('Digite um numero: '))
for c in range(1,11):
    
    r= n * c
    print('{} * {} = {}'.format(n,c,r))