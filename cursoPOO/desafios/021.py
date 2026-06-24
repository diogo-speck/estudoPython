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
        texto = f"[{self.cor}]{frase}"
        print(texto, end="") # imprime sem pular linha
        return texto # devolve a string
    
    def pular_linha(self, vezes=1):
        texto = "\n"*vezes
        print(texto, end="")
        return texto
    
c1 = Caneta("blue")
c1.escrever("Escrevendo em Azul")
c1.pular_linha(2)
c2 = Caneta("green")
c2.escrever("Escrevendo em Verde")
c3 = Caneta("red")
c3.escrever(" Escrevendo em Vermelho")