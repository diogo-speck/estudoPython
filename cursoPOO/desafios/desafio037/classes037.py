# Implemente uma Classe Mensagem, simulando um sistema de mensagem padronizadas
from rich import print, inspect
from rich.panel import Panel

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
        self._icone = "💬"
        self._cor = ""
    
    def mostrar(self):
        msg = Panel(f"[white on {self._cor}]{self._mensagem}[/]", title=f"{self._icone}  {self._tipo}  {self._icone}", style="")
        print(msg)

class Erro(Mensagem):
    def __init__(self, mensagem = "", tipo="Erro"):
        super().__init__(mensagem, tipo)
        self._icone = "🚫"
        self._cor = "red"

class Aviso(Mensagem):
    def __init__(self, mensagem = "", tipo="Aviso"):
        super().__init__(mensagem, tipo)
        self._icone = "⚠️"
        self._cor = "yellow"