# Exercício Herança, Abstração e Encapsulamento (ex005) Aprimorado

from rich import print, inspect
from cursoPOO.exercicios.ex005.classesEx005 import *
import json
from datetime import date

class Aluno(Pessoa):
    """
        Classe que instância um objeto chamado Aluno que atribui _nome, _nascimento (@ incluindo atributos validáveis) e
        @idade, além de ter um atributo de classe cursos_oficiais _curso(@) e um method add_curso(curso)
        ex. add_curso(curso)
    """

    cursos_oficiais = ["ADM","ADS", "ENG", "CONT"]

    def __init__(self, nome, nascimento, curso=None):
        idade = date.today().year - nascimento


        super().__init__(nome, idade)

        self._nascimento = nascimento
        self._curso = [curso.upper()] if curso else []
        Pessoa.alunos.append(nome)

    @property
    def idade(self):
        idade = date.today().year - self._nascimento
        if 0 < idade <= 122:
            self._idade = idade
            return idade
        else:
            raise ValueError(
                f"Ano inválido, o ano precisa estar entre {date.today().year - 123} e {date.today().year}."
            )

    @idade.setter
    def idade(self, _):
        raise PermissionError(
            "Você não pode alterar a idade, somente o ano de nascimento."
        )

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, ano):
        idade = date.today().year - ano
        if 0 < idade <= 122:
            self._nascimento = ano
        else:
            raise ValueError(
                f"Ano inválido, o ano precisa estar entre {date.today().year - 123} e {date.today().year}."
            )

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        with open("nomes.json", "r") as file:
            nomes = json.load(file)
            proibidos = nomes["nomes_proibidos"]
        if nome not in proibidos:
            self._nome = nome
        else:
            print("Nome proibido em cartório")

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, curso):
        curso_upper = curso.upper()
        if len(curso_upper) >= 3 and curso_upper not in self.cursos_oficiais:
            self.cursos_oficiais.append(curso_upper)
            print(f"Curso {curso_upper} adicionado à lista oficial.")
        else:
            print("Curso inválido ou já existente")


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





a1 = Aluno("Gustavo", 1978, "ADM")
print(a1.idade)
try:
    a1.idade = 90
except PermissionError as e:
    print(e)
a1.nascimento = 1943

c = input("Digite um curso para adicionar a sua grade curricular: ").upper()
a1.curso = c
a1.add_curso()
a1.nome = "Aborto"
inspect(a1, private=True, methods=True)