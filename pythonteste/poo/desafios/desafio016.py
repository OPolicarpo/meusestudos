'''crie a classe FUNCIONARIO, onde podemos cadastrar NOME,SETOR e CARGO.
 Crie tambem um metodo que permita ao funcionario se APRESENTAR'''

from rich import print
from rich import inspect

class Funcionario:
    def __init__(self,nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentar(self):
        return f':+1: Ola, sou [bold red on blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} na empresa curso em video'

c1= Funcionario('Policarpo', "Analista de dados",'servico')
print(c1.apresentar())
#inspect(c1)

c2 = Funcionario('Nathalia', 'Mulher da minha vida' , 'Casa')
print(c2.apresentar())

