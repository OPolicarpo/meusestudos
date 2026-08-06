'''crie um programa onde o usuario possa digitar varios valores numericos
e cadastre em uma lista. caso o numero ja existala dentro, ele nao sera adicionado. 
no final serao exibidos todos os valores unicos digitados em ordem crescente'''
valores = list()

while True:
    numero = int(input('Digite um valor '))
    print('Valor adicionado com sucesso!')
   # valores.append(int(input('Digite um valor ')))
    cond= input('Deseja continuar? S/N').upper()  
    if numero in valores:
        pass
    else:
        valores.append(numero)
    if cond != 'S' and cond != 'N':
        print('Opção invalida') 
    if cond == 'N' :
        break
print(f'Os valores adicionados são {valores}')