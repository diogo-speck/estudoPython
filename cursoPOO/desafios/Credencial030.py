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
        self.__hash = self.__criptografar(senha)
        self.__senha = senha.upper()
        del self.__senha      # apaga a senha após gerar o hash

    @property
    def senha(self):
        return self.__senha

    @senha.deleter
    def senha(self):
        # remove o atributo interno __senha
        del self.__senha

    @property
    def hash(self):
        return self.__hash

    @property
    def cifra(self):
        return self.__cifra

    def __criptografar(self, texto):
        resultado = ""
        for letra in texto.upper():
            if letra in self.letras:
                idx = (self.letras.index(letra) + self.__cifra) % 25
                resultado += self.letras[idx]
            else:
                resultado += letra
        return resultado

    def validar(self, senha):
        return self.__criptografar(senha) == self.__hash