'''crie um programa que leia as duas notas de um aluno e calcule sua media, mostrando a mensagem no final de acordo com a media atinfgida
media abaixo de 5 - reprovado
entre 5 e 6.9 - recuperacao
media 7 ou superior aprovado'''
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m= (n1+n2)/2
if m<5.0:
    print('Sua media foi de {} e voce esta: \033[31m REPROVADO \033[m'.format(m))
elif m>= 5.0 and m<6.9:
    print('Sua media foi de {} e voce esta: \033[33m EM RECUPERACAO \033[m'.format(m))
elif m>6.9:
    print('Sua media foi de {} e voce esta: \033[32m APROVADO \033[m'.format(m))