'''crie a classe GAMER, onde podemos cadastrat
NOME, NICK e os JOGOS FAVORITOS de uma pessoa.
crie tambem um metodo que permita mostrar a ficha do gammer.'''

from rich import print
from rich.panel import Panel
class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = list()


    def add_favorito(self, game):
        self.favoritos.append(game)
        self.favoritos = sorted(self.favoritos, key=str.lower)


    def ficha(self):
        conteudo = f"Nome real: {self.nome}"
        conteudo += f"\n Jogos Favoritos: "
        for nume, game in enumerate(self.favoritos):
            conteudo+= f"\n :video_game: [blue]{game}[/]"
        painel = Panel(conteudo, title=f"[yellow] Jogador {self.nick}[\]", width=40)
        print(painel)

    
j1= Gamer("Fabricio da Silva", "Detoonador") 
j1.add_favorito("Mario")
j1.add_favorito("fifa")
j1.ficha()

j2 = Gamer ("Poli", "triplex")
j2.add_favorito('Bomberman')
j2.add_favorito('pecman')
j2.add_favorito('batman')
j2.ficha()