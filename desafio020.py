#o mesmo professor do desafio anterior quer sortear a ordem de apresentacao de trabalhos dos alunos. faca um programa que leia o nome dos 4 alunos e mostre a ordem sorteada
import random
n1 = input ('Aluno 1: ')
n2 = input ('Aluno 2: ')
n3 = input ('Aluno 3: ')
n4 = input ('Aluno 4: ')
lista = [n1,n2,n3,n4]
random.shuffle(lista)
#usar o shufle faz com que ele embaralhe os numeros e ele solta uma lista sem repeticoes
print('A ordem de apresentacao sera \n {}'.format(lista))
