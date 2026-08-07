'''
crie um programa que leia o nome e duas notas de varios alunos e 
guarde tudo em uma lista composta
no final, mostre um boletin contendo a media de cada um e
permita que o usuario possa mostrar as notas de cada aluno individualmente
'''
alunos =[]
while True:
    cad = []
    nome = str(input('Digite seu nome: ')).upper()
    cad.append(nome)
    nota1 = float(input('Nota 1: '))
    cad.append(nota1)
    nota2 = float(input('Nota 2: '))
    cad.append(nota2)
    media=(nota1+nota2)/2
    cad.append(media)
    alunos.append(cad)
    cond = str(input('Deseja continuar? [S/N]')).upper()
    if cond == 'N': 
        break

print('-='*30)
for c in range (len(alunos)) :   
    print(f'{c}. Nome {alunos[c][0]}, media {alunos[c][3]}')
    escolha = input('deseja ver a nota de algum aluno?')
    c = escolha
print(c)
    
        
    




# 1Q - Quais são os dados de entrada necessários?
#nome do aluno e 2 notas
# 2Q - O que devo fazer com esses dados?
#
#
#
# 3Q - Quais são as restrições deste problema?
#guardar numa lista composta
#
#
# 4Q - Qual é o resultado esperado?
#mostrar um boletinho com as notas em media
# mostrar a nota individual de cada aluno
#
# 5Q - Qual é a sequência de passos para chegar ao resultado esperado?
#cadastrar aluno
#cadastrar nota
#S/N
# caucular a media
#mostrar a media com nome individual do aluno