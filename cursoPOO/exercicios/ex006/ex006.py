# Exercício Conta Bancária
class Conta:
    """
        Cria uma conta bancária e permite fazer depósitos e saques
    """
    def __init__(self, nome, id, saldo=0):
        self._titular = nome # Protegido (#)
        self.id = id # Público (+)
        self.__saldo = saldo # Privado (-)
        print(f"Conta {self.id} criada no nome de {self._titular}. Saldo atual R${self.__saldo:,.2f}")
    
    def __str__(self):
        return f"{self._titular} é o titular da conta {self.id}, seu saldo atual é de R${self.__saldo:,.2f}" # invés de .00

    def deposito(self,valor):
        valor = abs(valor)
        self.__saldo += valor
        print (f"{self._titular} recebeu R${valor:,.2f} em sua conta {self.id} e agora tem R${self.__saldo:,.2f} de saldo")
    
    def saque(self,valor):
        valor = abs(valor)
        if valor > self.__saldo:
            print (f"Saldo insuficiente em sua conta {self.id} {self._titular}, faça um depósito de pelo menos R${(valor - self.__saldo):,.2f}")
        else:
            self.__saldo -= valor
            print (f"{self._titular} sacou R${valor:,.2f} em sua conta {self.id} e agora tem R${self.__saldo:,.2f} de saldo")