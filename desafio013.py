#faca um algoritimo que leia o salario de um funcionario e mostre o seu novo salario com 15% de aumento.
nome=input('Digite seu nome de registro na empresa: ')
salario= float(input('digite o valor de salario atual: '))
aum= salario + salario/100*15
print('Parabens {}, voce acabou de ganhar um aumento de 15% e seu salaio atual e de {}'.format(nome,aum))
