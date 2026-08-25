# Declaracao de Classe
class Gafanhoto:
    """ Essa classe cria um gafanhoto, que e uma pessoa que tem essa idade.
    para criar uma nova pessoa, ude 
    variavel = nome idade"""
    def __init__(self, n = '', i = 0): #metodo construtor
        #atributos de instancia
        self.nome = n
        self.idade= i


    # metodo de instancia
    def aniversario(self):
        self.idade = self.idade + 1
    

    def __str__(self): #donder method
        return f'{self.nome} e Gafanhoto e tem {self.idade} anos de idade' 
#declaracao de objetos
#agora que eu to fazendo a criacao do objeto ou estanciaca

#g1 = Gafanhoto()

'''g1.nome = 'Policarpo' #g1.nome e um atributo
g1.idade = 34
g1.aniversario() #g1.an() e um metodo
print (g1.mensagem())

g2 = Gafanhoto('Maria', 17)
g2.aniversario()
print(g2.mensagem())'''

g1 = Gafanhoto('Mauro', 53)
g1.aniversario()
print(g1.__dict__)
print(g1.__class__)
#print(g1.__doc__) #dunter atribute

#self e um nome generico de um atributo de instancia

'''g3 = Gafanhoto()
print(g3.mensagem())'''
