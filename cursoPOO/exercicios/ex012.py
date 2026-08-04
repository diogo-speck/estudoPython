from abc import ABC, abstractmethod


class Animais(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def emitir_som(self):
        print(f"{self.__class__.__name__} está emitindo um som")

class Pato(Animais):
    def emitir_som(self):
        print("Quack Quack")

class Cachorro(Animais):
    def emitir_som(self):
        print("Au au")

class Gato(Animais):
    def emitir_som(self):
        print("Miau Miau")

class Galinha(Animais):
    def emitir_som(self):
        print("Pó pó")

class Raposa(Animais):
    def emitir_som(self):
       super().emitir_som()


class Spitz(Cachorro):
    def emitir_som(self):
        print("auauauauauauauau")

class PitBull(Cachorro):
    def emitir_som(self):
        print("Ruf ruf")


a1 = Pato()
a2 = Cachorro()
a3 = Gato()
a4 = Galinha()
a5 = Raposa()
a6 = Spitz()
a7 = PitBull()

a1.emitir_som()
a2.emitir_som()
a3.emitir_som()
a4.emitir_som()
a5.emitir_som()
a6.emitir_som()
a7.emitir_som()