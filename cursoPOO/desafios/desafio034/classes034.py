# Implemente uma Classe Funcionario, simulando um funcionário com seu salário e bônus salarial
from rich import print, inspect
from abc import ABC, abstractmethod

class Funcionario(ABC):
    """
        Classe abstrata que instancia um objeto chamado Funcionario onde recebe um nome e um salário
        Possui os atributos @nome (público) e @salario (privado)
        ex. f1 = Funcionario("nome", salario)
        Possui 1 method:
        calcular_bonus(valor)
        ex. f1.calcular_bonus(valor)
    """

    def __init__(self, nome:str, salario:float=0.0):
        self.nome = nome
        self._salario = salario
    

    @property
    def salario(self):
        return self._salario
    
    @salario.setter
    def salario(self, salario:float):
        if salario > self._salario:
            self._salario = salario
        else:
            raise ValueError("O novo salário precisa ser maior que o salário atual")


    @abstractmethod
    def calcular_bonus(self):
        pass

    @abstractmethod
    def __str__(self):
        pass



class Gerente(Funcionario): # 15%
    def __init__(self, nome:str, salario:float=0.0):
        super().__init__(nome, salario)
    
    def calcular_bonus(self):
        return self._salario*0.15
    
    def __str__(self):
        return f"{self.nome} ganha R${self._salario:,.2f} e por ser {self.__class__.__name__} o bônus será de R${(self.calcular_bonus()):,.2f}"


class Designer(Funcionario): # 8%
    def __init__(self, nome:str, salario:float=0.0):
        super().__init__(nome, salario)
    
    def calcular_bonus(self):
        return self._salario*0.08

    def __str__(self):
        return f"{self.nome} ganha R${self._salario:,.2f} e por ser {self.__class__.__name__} o bônus será de R${(self.calcular_bonus()):,.2f}"


class Desenvolvedor(Funcionario): # 10%
    def __init__(self, nome:str, salario:float=0.0):
        super().__init__(nome, salario)
    
    def calcular_bonus(self):
        return self._salario*0.1
    
    def __str__(self):
        return f"{self.nome} ganha R${self._salario:,.2f} e por ser {self.__class__.__name__} o bônus será de R${(self.calcular_bonus()):,.2f}"