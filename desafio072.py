'''crie um programa que tenha uma tupla totalmente preenchina com uma contagem por extenso de 0 a 220
seu programa devera ler um nomero pelo teclado entre 0 e 20 e  mostralo por extenso>'''
numero = ('zero', 'um', 'dois', 'tres', 
          'quatro', 'cinco', 'seis', 'sete', 'oito',
            'nove', 'dez', 'onze', 'doze', 'treze', 
            'quatorze', 'quinze', 'dezeseis', 'dezesete',
              'dezoito','dezenove','vinte' )

n= int(input('Digite um numero de 0 a 20 '))
print(f'{numero[n]}')