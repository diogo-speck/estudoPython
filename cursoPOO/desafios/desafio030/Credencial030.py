# Implemente uma Classe Credencial, simulando o funcionamento de uma hash com Cifra de César
from rich import print, inspect
import random, string

class Credencial:
    """
        Classe que instancia um objeto chamado Credencial onde recebe uma 'String' e devolve outra criptografada
        OBS: Números e caracteres especiais não sofrem variação
        Possui os atributos @senha (público) e __hash/__cifra (privado)
        ex. c1 = Credencial("senha")
        Possui 1 method:
        validar(senha)
        ex. c1.validar("123")
    """

    letras = list(string.ascii_uppercase)

    def __init__(self, senha=""):
        self.__cifra = random.randint(1,26)
        senha = senha.strip().upper()
        self.__hash = self.__criptografar(senha)
        del senha    # apaga a senha após gerar o hash

    @property
    def senha(self):
        nsenha = ""
        for l in self.__senha.strip():
            l = l.upper()
            nsenha+=l
        self.__senha = nsenha
        return self.__senha

    @senha.deleter
    def senha(self):
        # remove o atributo interno __senha
        del self.__senha

    def __criptografar(self, texto):
        resultado = ""
        for letra in str(texto):
            if letra in self.letras:
                idx = (self.letras.index(letra) + self.__cifra) % 25
                resultado += self.letras[idx]
            else:
                resultado += letra
        return resultado

    def validar(self, senha):
        senha = senha.strip().upper()
        return self.__criptografar(senha) == self.__hash