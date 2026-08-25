''' crie uma classe LIVRO que vai simular a 
PASSAGEM DE PAGINA de um livro, considerando tambem
se o usuario chegou ao fim da leitura'''
from rich import print
class Livro:
    def __init__(self, nome, pag):
        self.titulo = nome
        self.totalpage = pag
        self.pag_atual = 1


        print(f':open_book: Voce acabou de abrir o livro {self.titulo} que tem {self.totalpage} paginas no total. Voce agora esta na pagina {self.pag_atual}')

    
    def avancar_paginas(self, qtd = 1):
        cont = 0
        for pg in range (0, qtd, 1):
            self.pag_atual +=1
            print(f'Pag{self.pag_atual} :arrow_forward: ', end='')
            cont += 1
        print(f'[blue]Voce avancou[\] {cont} paginas e agora esta na [yellow]pagina {self.pag_atual}[\]')
        if self.fim_do_livro():
            print(f':closed_book: [red] Voce chegou ao final do livro {self.titulo} [/red]' )

    
    def fim_do_livro(self) -> bool:
        if self.pag_atual == self.totalpage:
            return True
        else:
            return False


l1 = Livro("10 coisas que aprendi", 10)
l1.avancar_paginas(11)