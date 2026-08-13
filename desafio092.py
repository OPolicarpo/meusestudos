'''crie um programa que leia nome, ano de nascimento e carteira de trabalho e
cadastreos com idade em um dicionario caso a CTPS for diferente de 0
o dicionario recebera tambem o ano de contratacao e o salario, 
calcule e acrescente alem da idade, com quantos anos a pessoa se aposenta
base = 35 anos de contribuicao''' 

cad = dict()
while True:
    cad['nome'] = str(input('Nome: '))
    cad['idade'] = int(input('Ano de nascimento: '))
    cad['ano']= 2026 - cad['idade'] 
    cad['carteira']= int(input('Carteira de trabalho (0 nao tem): '))
    if cad['carteira'] == 0:
        print(cad)
        break
    cad['assina'] = int(input('Ano da contratacao: '))
    cad['apo'] = (cad['assina'] + 35) - cad['idade']
    cad['salario'] = int(input('salario: '))
    #print(cad)
    print(f'Nome tem valor {cad['nome']}')
    print(f'A idade tem valor {cad['ano']}')
    print(f'ctps {cad['carteira']}')
    print(f'Ano da contratacao {cad['assina']}')
    print(f'O salario tem valor de {cad['salario']} ')
    print(f'Vai se aposentar com {cad['apo']} anos')
    break

