'''refaca o desafio 51, lendo o rimeiro termo e a razao de uma PA, mostrando os 10 primeiros termos da progressao usando a estrutura while'''
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
cont= 0
print(termo)
while cont != 0:
    termo = termo + razao
    cont = cont + 1
    print (termo)
    qt = int(input('quantos termos a mais deseja mostrar: '))
    if qt != 0:
        for cont in range (qt):
            termo = termo + razao
            cont = cont + 1
        print(termo)
    elif qt == 0:
         print('Fim')