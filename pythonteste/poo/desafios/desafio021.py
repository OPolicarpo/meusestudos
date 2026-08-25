'''crie uma classe CANETA, que simule o funcionamento de uma 
CANETA COLORIDA, podendo ESCREVER frases na cor relativa,'''
from rich import print
class Caneta:
    def __init__(self, cor = 'azul'):
        match cor.lower().strip():
            case "azul":
                escolha = "[blue]"
            case "vermelho" | "vermelha":
                escolha = "[red]"
            case "verde":
                escolha = "[green]"
            case _:
                escolha = "[white]"
            
        self.cor = escolha
        self.tampada = True


    def escrever (self, msg):
        if self.tampada:
            print(f":prohibited: A {self.cor} CANETA[/] esta tampada!")
        else:
            print(f"{self.cor}{msg}[/]", end='')

    
    def quebra_linha(self, qdt = 1):
        print("\n"*qdt, end='')

    def tampar(self):
        self.tampada = True

    def destampar(self):
        self.tampada = False


c1 = Caneta("azul")
c2 = Caneta("vermelho")
c3 = Caneta("verde")
c1.destampar()
c2.destampar()

c1.escrever("Ola, mundo")
c2.escrever("Funciona!")
c3.escrever("Deu certo")

