'''Crie uma classe PRODUTO, onde podemos 
cadastrar NOME e o PRECO. Crie tambem um METODO que mostre uma 
ETIQUETA de preco do produto.'''
from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def etiqueta (self):
        linha = ('-'*30)
        print(
        Panel(f'{self.nome} \n {linha} \n {self.preco}'.center(len(linha)), title = 'PRODUTO', expand=False)
        )


p1 = Produto('Iphone 17 pro max', 7_500)
p1.etiqueta()

p2 = Produto('PS4', 1_800.85)
p2.etiqueta()