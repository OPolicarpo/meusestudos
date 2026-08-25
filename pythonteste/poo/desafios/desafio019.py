''' crie uma classe LIVRO que vai simular a 
PASSAGEM DE PAGINA de um livro, considerando tambem
se o usuario chegou ao fim da leitura'''
from rich import print
class Livro:
    def __init__(self, nome, pag):
        self.nome = nome
        self.page = pag


    def avancar (self):
        for i in range(1, avancar + 1):
           
            print(f'Pag{i} ->')



#programa
l1 = Livro ('!0 coisas que aprendi', 20)
l1.avancar(5)