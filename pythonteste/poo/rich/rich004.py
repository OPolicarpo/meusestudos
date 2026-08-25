from rich import print
from rich import inspect

class ContaBancaria: 
    '''
    Criar uma conta bancaria e permite fazer saques e depositos
    '''
    def __init__(self, id, nome, saldo=0):
        self.id = id
        self.titular = nome
        self.saldo =saldo
        print(f'Conta {self.id} criada com sucesso. Saldo Atual de R${self.saldo:,.2f}')
    

    def __str__(self):
        return f'A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo'
        

    def deposito (self, valor):
        self.saldo += valor
        print(f'Deposito autorizado de R${valor:,.2f} na conta {self.id}')


    def sacar(self,valor):
        if valor > self.saldo:
            print(f'Saque negado de R${valor:,.2f} na conta {self.id}: SALDO INSUFICIENTE')
        else:
            self.saldo-= valor
            print(f'Saque de R${valor:,.2f} autorizado na conta {self.id}')
    
c1 = ContaBancaria(112, 'Policarpo' , 3000)
c1.deposito(500)
c1.sacar(7000)


inspect(c1.__getstate__())