# Implemente uma Classe Mensagem, simulando um sistema de mensagem padronizadas
from rich import print, inspect

class Mensagem():
    """
        Classe que instancia um objeto chamado Mensagem onde recebe um texto e um tipo
        Possui os atributos #mensagem (privado), #tipo (privado) e #icone (privado)
        ex. m1 = Mensagem("texto", tipo)
        Possui 1 method:
        mostrar()
        ex. m1.mostrars()
    """

    def __init__(self, mensagem="", tipo="Mensagem"):
        self._mensagem = mensagem
        self._tipo = tipo
        self._icone = ""
    
    def mostrar(self):
        print(f"{self._tipo}: {self._mensagem} {self._icone}")

class Erro(Mensagem):
    def __init__(self, mensagem = "", tipo="Erro"):
        super().__init__(mensagem, tipo)
        self._icone = "🚫"

class Aviso(Mensagem):
    def __init__(self, mensagem = "", tipo="Aviso"):
        super().__init__(mensagem, tipo)
        self._icone = "❗"