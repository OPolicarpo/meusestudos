'''crie a classe CHURRASCO, onde seja
possivel informar QUANTAS PESSOAS vao participar e mostre
QUANTO DE CARNE deve ser comprado, 
o CUSTO TOTAL do churrasco e o preco por PESSOA.'''
from rich import print
from rich.panel import Panel
class Churrasco:
    def __init__(self,titulo, quant, kg = 0, custo = 0, cada = 0):
        self.titulo = titulo
        self.quant = quant
      

    def informar(self):
        kg = self.quant * 0.400
        custo = kg * 82.40
        cada = custo / self.quant
        print(Panel(f'Analisando o [green]{self.titulo}[/] com [blue]{self.quant}[/]\nCada participante comeca 0.4kg e cada kg de carne custa R$82.40 \n Recomendo comprar {kg} kg de carne \n o custo total sera de R${custo:.2f} \n Cada pessoa pagara R${cada}', title='Churras dos amigos'))


c1= Churrasco('Churras dos amigos', 15)
c1.informar()

#considere / 400g por pessoa / preco do kilo 82,40