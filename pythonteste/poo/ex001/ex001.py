# Declaracao de Classe
class Gafanhoto:
    def __init__(self): #metodo construtor
        #atributos de instancia
        self.nome = ''
        self.idade= 0


    # metodo de instancia
    def aniversario(self):
        self.idade = self.idade + 1
    

    def mensagem(self):
        return f'{self.nome} e Gafanhoto(A) e tem {self.idade} anos de idade '
        #essa declaracao de cima e o molde e agora eu preciso instanciar um objeto

#declaracao de objetos
#agora que eu to fazendo a criacao do objeto ou estanciaca

g1 = Gafanhoto()

g1.nome = 'Policarpo' #g1.nome e um atributo
g1.idade = 34
g1.aniversario() #g1.an() e um metodo
print (g1.mensagem())

g2 = Gafanhoto()
g2.nome = 'Nathalia'
g2.idade = 21
g2.aniversario()
print(g2.mensagem())

#self e um nome generico de um atributo de instancia
