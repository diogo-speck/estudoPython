# Implemente duas Classes JSON e XML para exportar dados de maneira funcional
from desafios.desafio039.classes039 import *
import random


class JSON():
    """
        Classe que exportar dados de maneira funcional em formato JSON
        Possui o método exportar(objeto())
    """
    def exportar(self, objeto):
        pass



class XML():
    """
        Classe que exportar dados de maneira funcional em formato XML
        Possui o método exportar(objeto())
    """
    def exportar(self, objeto):
        pass


class Login():
    def __init__(self, user, email, senha=""):
        if not validar_dado(User(), user):
            self.user = str(random.randint(10000, 99999999999999999999)).zfill(20)
            print(f"Seu novo usuário: {self.user}")
        else:
            self.user = user

        while not validar_dado(Email(), email):
            email = input("Digite outro e-mail: ")
        self.email = email

        senha = user+"_123"
        while not validar_dado(Senha(), senha):
            senha = input("Digite outro senha: ")
        self._senha = senha

    def __str__(self):
        return f'"User" : "{self.user}"; "Email" : "{self.email}"; "Senha" : "{self._senha}"'

class Estudante():
    def __init__(self, nome, serie="1ª", curso=None):
        self.nome = nome
        self.serie = serie
        self.curso = curso

    def __str__(self):
        return f'"Nome" : "{self.nome}"; "Serie" : "{self.serie}"; "Curso" : "{self.curso}"'



def exportar_dados(tipo, objeto):
    tipo.exportar(objeto)