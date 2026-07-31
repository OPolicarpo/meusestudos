#escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento,
#para salarios superio a 1250, aumenta 10% e inferiores ou iguais 15%
sal=float(input('Digite o seu salario atual: '))
if sal > 1250:
    salat = (sal+ sal/100*10)
    print('o seu salario passara a ser {}'.format(salat))
else:
    salat =(sal+sal/100*15)
    print('O seu salario passara a ser {}'.format(salat))


s1= float(input('Digite o seu salario atual: '))
if s1 <= 1250:
    novo= s1 +(s1 *15/100)
else:
    novo = s1+(s1*10/100)
print('Quem ganhava {:.2f} passa a ganhar {:.2f} agora!'.format(s1,novo))