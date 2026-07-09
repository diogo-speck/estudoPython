# Diagrama de Classes: Polígono (abstrato) com quantidade de lados sendo um atributo e perímetro e área sendo métodos
# abstratos; Além disso, terá pelo menos 2 classes filhas quadrado com lado e circulo com raio

from abc import ABC, abstractmethod
import math
from rich import print, inspect

class Poligono(ABC):

    def __init__(self,lados):
        self.qtd_lados = lados

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Quadrado(Poligono):

    def __init__(self, comprimento=1):
        super().__init__(4)
        self.comprimento = comprimento
        print("Quadrado criado")

    def perimetro(self):
        return f"O perímetro de um Quadrado de lado {self.comprimento} é {self.comprimento*self.qtd_lados}"

    def area(self):
        return f"A área de um Quadrado de lado {self.comprimento} é {self.comprimento**2}"

class Circulo(Poligono):

    def __init__(self, raio=1):
        super().__init__(0)
        self.raio = raio
        print("Círculo criado")

    def perimetro(self):
        return f"O perímetro de um Círculo de raio {self.raio} é {2*math.pi*self.raio:.1f}"

    def area(self):
        return f"A área de um Círculo de raio {self.raio} é {math.pi*self.raio**2:.1f}"



# p0 = Poligono(1) não é possível instanciar
# inspect(p0)

p1 = Quadrado(12)
print(p1.perimetro())
print(p1.area())

p2 = Circulo()
print(p2.perimetro())
print(p2.area())

#inspect(p1)
#inspect(p2)