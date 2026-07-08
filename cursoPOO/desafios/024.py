# Diagrama de Classes de uma Cafeteira: BebidaQuente (abstrato) com preparar e ferver_agua sendo concretos e
# misturar e servir sendo métodos abstratos; Além disso, terá 3 classes filhas Cafe, Cha e Leite

from abc import ABC, abstractmethod
from rich import print, inspect

class BebidaQuente(ABC):
    def __init__(self):
        pass

    def preparar(self) -> None:
        print("--- Iniciando o Preparo ---")
        self.ferver_agua()
        self.misturar()
        self.servir()
        print("--- Bebida Pronta ---")

    def ferver_agua(self):
        print("1. Fervendo água a 100ºC.")

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass


class Cafe(BebidaQuente):
    def __init__(self):
        super().__init__()

    def misturar(self):
        print("2. Passando água pressurizada pelo pó de café moído.")

    def servir(self):
        print("3. Expresso pronto")


class Cha(BebidaQuente):
    def __init__(self):
        super().__init__()

    def misturar(self):
        print("2. Mergunlhando o sachê de ervas na água.")

    def servir(self):
        print("3. Servindo na caneca de porcelana com limão.")


class Leite(BebidaQuente):
    def __init__(self):
        super().__init__()

    def misturar(self):
        print("2. Passando vapor pressurizado pelo bico de leite.")

    def servir(self):
        print("3. Leite vaporizado pronto.")


class CafeComLeite(Cafe,Leite):
    def misturar(self):
        Cafe.misturar(self)
        Leite.misturar(self)
        print("3. Fazendo a latte art (misturando o leite no café)")

    def servir(self):
        print("4. Servindo café com leite.")



cafeP = Cafe()
cafeP.preparar()
print()
chazin = Cha()
chazin.preparar()
print()
pingado = CafeComLeite()
pingado.preparar()