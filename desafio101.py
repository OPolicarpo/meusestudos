'''crie um programa que tenha uma funcao chamada VOTO() que
vai receber como parametro o ano de nascimento de uma pessoa, 
RETORNANDO um valor LITERAL indicando se uma pessoa tem voto
OPCIONAL, NEGADO OU OBRIGATORIO NAS ELEICOES'''
from datetime import datetime
def idade(num):
    num = datetime.now().year - num
    print(f'Com {idade(num)} anos :', end='')
    if num < 16:
        print('VOTO NEGADO')
    elif num < 18 or num > 55:
        print('VOTO OPCIONAL')
    else:
        print('VOTO OBRIGATORIO')
    return idade


idade = int(input('Em que ano voce nasceu?'))
idade(num)


