# Crie a Classe Caneta, que simule o funcionamento de uma caneta colorida, podendo escrever frases na cor relativa.
from rich import print

class Caneta:
    """
        Classe que instancia um objeto chamado Caneta e atribui a ele uma cor
        ex. objeto = Caneta("color")
        Possui um método escrever() para escrever qualquer texto com a cor da caneta
        ex. print(objeto.escrever("Texto"))
    """
    def __init__(self, cor):
        self.cor = cor

    def escrever(self, frase):
        return f"[{self.cor}]{frase}"
    
c1 = Caneta("blue")
print(c1.escrever("Escrevendo em Azul\n"))
c2 = Caneta("green")
print(c2.escrever("Escrevendo em Verde\n"))
c3 = Caneta("red")
print(c3.escrever("Escrevendo em Vermelho\n"))