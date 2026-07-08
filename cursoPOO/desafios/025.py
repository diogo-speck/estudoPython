# Diagrama de Classes de Frete: Transporte (abstrato) com atributos de distância e frete sendo concretos e
# calc_frete sendo um abstractmethod; Além disso, terá 3 classes filhas Moto, Caminhão e Drone

from abc import ABC, abstractmethod
from rich import print, inspect

class Transporte(ABC):
    def __init__(self, km, item):
        self.distancia = km
        self.frete = item

    @abstractmethod
    def calc_frete(self):
        pass

class Moto(Transporte): # Livre
    fator = 0.5
    def calc_frete(self):
        return f"Para fretar um(a) {self.frete} de {type(self).__name__} em {self.distancia}Km é necessário R${self.distancia*self.fator:,.2f}"

class Caminhao(Transporte): # Mínimo 50km
    fator = 1.2
    def calc_frete(self):
        if self.distancia >= 50:
            return f"Para fretar um(a) {self.frete} de {type(self).__name__} em {self.distancia}Km é necessário R${self.distancia * self.fator:,.2f}"
        else:
            return f"Não compensa fretar um(a) {self.frete} de {type(self).__name__} por conta da distância curta de {self.distancia}Km"

class Drone(Transporte): # Máximo 10km
    fator = 9.5
    def calc_frete(self):
        if self.distancia <= 10:
            return f"Para fretar um(a) {self.frete} de {type(self).__name__} em {self.distancia}Km é necessário R${self.distancia * self.fator:,.2f}"
        else:
            return f"O {type(self).__name__} não consegue fretar um(a) {self.frete} por {self.distancia}Km por conta da sua bateria"


e1 = Moto(20, "remédio")
print(e1.calc_frete())

e2 = Caminhao(80, "mudança")
print(e2.calc_frete())

e3 = Drone(8, "delivery")
print(e3.calc_frete())