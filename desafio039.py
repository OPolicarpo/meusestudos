'''faca um programa que leia o ano de nascimento e informe de acordo com a sua idade
- se ele ainda vai se alistar no tg
-se esta na hora de se alistar no tg
se ja passou o tempo do alistamento'''

idade = int(input('Digite sua idade: '))
f=0
if idade<18:
    f= 18 - idade
    print('Voce ainda vai se alistar ao servico militar, faltam {} anos para voce se alistar'.format(f))
elif idade == 18:
    print(' Esta na hora de voce se alistar no TG')
elif idade>18:
    f= idade - 18
    print('Voce passou {} anos do prazo de alistamento'.format(f))
