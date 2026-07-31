#um professor quer sortear um dos seus quatro alunos para apagar o quadro. faca um programa que ajude ele lendo o nome deles e escrevendo o nome do escolhido.
import random

n1 = input ('Aluno 1: ')
n2 = input ('Aluno 2: ')
n3 = input ('Aluno 3: ')
n4 = input ('Aluno 4: ')
list = [n1,n2,n3,n4]
ran = random.choice(list)
print('O Aluno escolhido para apagar o quadro foi {}'.format(ran))

