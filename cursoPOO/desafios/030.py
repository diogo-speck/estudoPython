# Implemente uma Classe Credencial, simulando o funcionamento de uma hash SHA256 (criptografia) / Cifra de César
from rich import print, inspect
import random, string

class Credencial:
    """
        Classe que instancia um objeto chamado Credencial onde recebe uma 'String' e devolve outra criptografada
        Possui os atributos @senha (público) e __hash/__cifra (privado)
        ex. c1 = Credencial("senha")
        Possui 1 method:
        validar(senha)
        ex. c1.validar("123")
    """

    letras = list(string.ascii_uppercase)

    def __init__(self, senha=""):
        self.__cifra = random.randint(1,26)
        self.senha = senha # Chama o 'Setter'

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, valor):
        self.__senha = valor.upper()
        self.__hash = self.__criptografar(self.__senha)

    def __criptografar(self, texto):
        resultado = ""
        for letra in texto.upper():
            if letra in self.letras:
                idx = (self.letras.index(letra) + self.__cifra) % 26
                resultado += self.letras[idx]
            else:
                resultado += letra
        return resultado

    def validar(self, senha):
        return self.__criptografar(senha) == self.__hash


c1 = Credencial("Diogo")
c1.senha = "Diogo"
print(c1.senha)
inspect(c1, private=True, methods=True)
c1.validar("dIoGo")
print(c1.senha)
print("Senha original:", c1.senha)
print("Validação correta:", c1.validar("Diogo"))  # True
print("Validação errada:", c1.validar("123"))     # False