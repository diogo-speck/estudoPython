from rich import print
from rich import inspect

class Conta:
    """
        Cria uma conta bancária e permite fazer depósitos e saques
    """
    def __init__(self, nome, id, saldo=0):
        self.titular = nome
        self.id = id
        self.saldo = saldo
        print(f"Conta {self.id} criada no nome de {self.titular}. Saldo atual R${self.saldo:,.2f}")
    
    def __str__(self):
        return f"{self.titular} é o titular da conta {self.id}, seu saldo atual é de R${self.saldo:,.2f}" # invés de .00

    def deposito(self,valor):
        self.saldo += valor
        print (f"{self.titular} recebeu R${valor:,.2f} em sua conta {self.id} e agora tem R${self.saldo:,.2f} de saldo")
    
    def saque(self,valor):
        if valor > self.saldo:
            print (f"Saldo insuficiente em sua conta {self.id} {self.titular}, faça um depósito de pelo menos R${(valor-self.saldo):,.2f}")
        else:
            print (f"{self.titular} sacou R${valor:,.2f} em sua conta {self.id} e agora tem R${self.saldo:,.2f} de saldo")
            self.saldo -= valor

inspect(int) #, all=True
# print(int.__doc__)
# print(int.__dict__)
c2 = Conta("José", 2, 500)
# inspect(Conta, all=True)
inspect(c2)