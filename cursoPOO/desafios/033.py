# Exercício Herança, Abstração e Encapsulamento (ex005) Aprimorado

from cursoPOO.exercicios.ex005.classesEx005 import *
from rich import print, inspect

class Aluno(Pessoa):
    """
        Classe que instância um objeto chamado Aluno que atribui _nome, _nascimento (@ incluindo atributos validáveis) e
        @idade, além de ter um atributo de classe cursos_oficiais _curso(@) e um method add_curso(curso)
        ex. add_curso(curso)
    """

    cursos_oficiais = ["ADM","ADS", "ENG", "CONT"]

    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self._nascimento = 2026-self.idade
        self.curso = [curso]
        Aluno.alunos.append(nome)


    def add_curso(self, curso):
        self.cursos_oficiais.append(curso.upper())
        print(f"Cursos disponíveis: {self.cursos_oficiais}")
        escolha = input("Escolha o curso que deseja fazer: ").upper()
        if escolha in self.cursos_oficiais:
            self.curso.append(curso)
            print(f"Seus cursos: {self.curso}")
        else:
            print(f"Curso não encontrado")

    def estaNaAcademia(self):
        return False



a1 = Aluno("Maria", 26, "ADM")
inspect(a1, private=True, methods=True)
a1.add_curso("Moda")