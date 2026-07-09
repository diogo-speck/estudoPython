# Diagrama de Classes de Frete: Transporte (abstrato) com atributos de distância e frete sendo concretos e
# calc_frete sendo um abstractmethod; Além disso, terá 3 classes filhas Moto, Caminhão e Drone

from abc import ABC, abstractmethod
from rich import print, inspect
from rich.table import Table

class Transporte(ABC):
    def __init__(self, km, item="item"):
        self.distancia = km
        self.frete = item

    @abstractmethod
    def calc_frete(self):
        pass

class Moto(Transporte): # Livre
    fator = 0.5
    def calc_frete(self):
        return f"Para fretar {self.distancia} Km é necessário [green]R${self.distancia*self.fator:,.2f}"

class Caminhao(Transporte): # Mínimo 50km
    fator = 1.2
    def calc_frete(self):
        if self.distancia >= 50:
            return f"Para fretar {self.distancia} Km é necessário [green]R${self.distancia * self.fator:,.2f}"
        else:
            return f"Não compensa fretar a distância de {self.distancia}Km"

class Drone(Transporte): # Máximo 10km
    fator = 9.5
    def calc_frete(self):
        if self.distancia <= 10:
            return f"Para fretar {self.distancia} Km é necessário [green]R${self.distancia * self.fator:,.2f}"
        else:
            return f"Distância de {self.distancia} Km muito longa para fretar"


e1 = Moto(20, "remédio")
e1.calc_frete()
e2 = Caminhao(80, "mudança")
e2.calc_frete()
e3 = Drone(8, "delivery")
e3.calc_frete()

dist = 80

viagens = [Moto(dist), Caminhao(dist), Drone(dist)]

tabela = Table(title="Tabela de Fretes")
tabela.add_column("Distância", justify="center")
tabela.add_column("Tipo", justify="center")
tabela.add_column("Frete", justify="left")

for viagem in viagens:
    tabela.add_row(f"{viagem.distancia} Km", f"{type(viagem).__name__}", f"{viagem.calc_frete()}")

print(tabela)