# Implemente uma Classe Pagamento, simulando um pagamento de diferentes formas
from rich import print, inspect
from abc import ABC, abstractmethod

class Pagamento(ABC):
    """
        Classe abstrata que instancia um objeto chamado Pagamento onde recebe um valor
        Possui os atributos -_valor (privada) e +@fvalor (público)
        ex. finalizar_compra(metodo, valor)
        Possui 1 abstractmethod:
        pagar(valor)
        ex. p1.pagar()
    """

    def __init__(self, valor:float=0.0):
        self._valor = valor
    
    @abstractmethod
    def pagar(self):
        pass

    @property
    def fvalor(self):
        return f"R${self._valor:,.2f}"


class Boleto(Pagamento):
    def __init__(self, valor:float=0.0):
        super().__init__(valor)
        
    def pagar(self):
        print(f"Você pagou {self.fvalor} no boleto")


class Pix(Pagamento):
    def __init__(self, valor:float=0.0):
        super().__init__(valor)
        
    def pagar(self):
        print(f"Você pagou {self.fvalor} no pix")


class Cartao(Pagamento):
    def __init__(self, valor:float=0.0):
        super().__init__(valor)
        
    def pagar(self):
        tipo = input(f"Você escolheu pagar {self.fvalor} no cartão. Débito ou Crédito (d/c)? ")
        if tipo == 'd':
            print(f"{self.fvalor} debitado no seu cartão de débito")
        else:
            print(f"{self.fvalor} creditado no seu cartão de crédito")


class Dinheiro(Pagamento):
    def __init__(self, valor:float=0.0):
        super().__init__(valor)
        
    def pagar(self):
        troco = float(input(f"Você pagou {self.fvalor} no dinheiro. Troco para quanto? "))
        if troco >= self._valor:
            print(f"Seu troco será R${(troco-self._valor):,.2f} (Total: {self.fvalor})")
        else:
            print(f"Quantia inválida, não daremos troco!")

    
def finalizar_compra(metodo, valor):
    metodo._valor = valor
    metodo.pagar()