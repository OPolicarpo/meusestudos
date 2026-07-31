'''melhore o desafio 061, perguntando para o usuario se ele quer mostrar mais alguns termos. o programa encerra quado ele disser que quer mostrar 0 termos'''
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
cont= 0
print(termo)
while cont < 9:
    termo = termo + razao
    cont = cont + 1
    print (termo)
qt = int(input('quantos termos a mais deseja mostrar: '))
while qt != 0:
    for i in range (qt):
        termo = termo + razao
        print(termo)
    qt = int(input('quantos termos a mais deseja mostrar: '))
print('Fim')