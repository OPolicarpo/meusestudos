sexo = str(input('Qual seu sexo [F] ou [M]: ')).upper()
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Qual seu sexo [F] ou [M]: ')).upper()
if sexo == 'M':
        print ('seu sexo e masculino!')
elif sexo == 'F':
        print('Seu sexo e Feminino')
