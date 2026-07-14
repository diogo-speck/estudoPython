# Exercício Herança, Abstração e Encapsulamento (ex005) Aprimorado

from rich import print, inspect
from cursoPOO.exercicios.ex005.classesEx005 import *
import json

class Aluno(Pessoa):
    """
        Classe que instância um objeto chamado Aluno que atribui _nome, _nascimento (@ incluindo atributos validáveis) e
        @idade, além de ter um atributo de classe cursos_oficiais _curso(@) e um method add_curso(curso)
        ex. add_curso(curso)
    """

    cursos_oficiais = ["ADM","ADS", "ENG", "CONT"]

    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self._nome = nome
        self._idade = idade
        self._nascimento = 2026-idade
        self._curso = [curso] if curso else []
        Pessoa.alunos.append(nome)


    def add_curso(self, curso=None):
        print(f"Cursos disponíveis: {self.cursos_oficiais}")
        if curso is None:
            escolha = input("Escolha o curso que deseja fazer: ").upper()
        else:
            escolha = curso.upper()
        if escolha in self.cursos_oficiais and escolha not in self._curso:
            self._curso.append(escolha)
            print(f"Seus cursos: {self._curso}")
        else:
            print(f"Curso não encontrado ou já adicionado")

    def estaNaAcademia(self):
        return False


    @property
    def nome(self):
        return self._nome

    @property
    def idade(self) -> int:
        return self._idade

    @property
    def curso(self):
        return self._curso

    @nome.setter
    def nome(self, nome):
        with open("nomes.json", "r") as file:
            nomes = json.load(file)
            proibidos = nomes["nomes_proibidos"]
        if nome not in proibidos:
            self._nome = nome
        else:
            print("Nome proibido em cartório")

    @idade.setter
    def idade(self, idade: int):
        if 1 <= idade <= 120:
            self._idade = idade
        else:
            print("Idade inválida")

    @curso.setter
    def curso(self, curso):
        curso_upper = curso.upper()
        if len(curso_upper) >= 3 and curso_upper not in self.cursos_oficiais:
            self.cursos_oficiais.append(curso_upper)
            print(f"Curso {curso_upper} adicionado à lista oficial.")
        else:
            print("Curso inválido ou já existente")



a1 = Aluno("Maria", 26, "ADM")
c = input("Digite um curso para adicionar a sua grade curricular: ").upper()
a1.curso = c
a1.add_curso()
a1.nome = "Aborto"
a1.idade = -25
inspect(a1, private=True, methods=True)