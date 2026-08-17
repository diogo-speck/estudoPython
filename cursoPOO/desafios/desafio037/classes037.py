# Implemente uma Classe Funcionario, simulando um funcionário com seu salário e bônus salarial
from rich import print, inspect
from abc import ABC

class Funcionario(ABC):
    """
        Classe abstrata que instancia um objeto chamado Funcionario onde recebe um nome e um salário
        Possui os atributos @nome (público) e @salario (privado)
        ex. f1 = Funcionario("nome", salario)
        Possui 1 method:
        calcular_bônus(valor)
        ex. f1.calcular_bônus(valor)
    """

    def __init__(self):
        pass