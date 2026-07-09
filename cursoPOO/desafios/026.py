# Diagrama de Classes de Salários: Funcionario (abstrato) com atributos de nome, sal_bruto e salario sendo concretos e
# sal_min e inss sendo atributos de classe. Além disso, terá calc_sal sendo um abstractmethod e analisar_sal.
# Depois terão 2 classes filhas Mensalista e Horista com os seus atributos de valor_hora e horas_trab

from abc import ABC, abstractmethod
from rich import print, inspect
from rich.panel import Panel

class Funcionario(ABC):
    SAL_MIN = 1621
    INSS = 7.5  # %
    def __init__(self, nome, salario=0):
        self.nome = nome
        self.sal_bruto = salario
        self.sal_liq = Funcionario.SAL_MIN

    @abstractmethod
    def calc_sal(self):
        pass

    def analisar_sal(self):
        print("Vamos analisar seu salário")
        print(self.calc_sal())
        analise =  Panel(f"O salário líquido mensal do(a) [magenta]{type(self).__name__}(a)[/] [blue]{self.nome}[/] é de [green]R${self.sal_liq}[/], que equivale a [yellow]{self.sal_liq/Funcionario.SAL_MIN:.2f} salários mínimos", width=55)
        return analise

class Mensalista(Funcionario): # CLT paga INSS
    def __init__(self, nome, salario=0):
        super().__init__(nome, salario)
        print(f"O(a) {type(self).__name__} {self.nome} trabalha no modelo CLT")

    def calc_sal(self):
        if self.sal_bruto * (1 - (Funcionario.INSS / 100)) > Funcionario.SAL_MIN:
            self.sal_liq = self.sal_bruto * (1 - (Funcionario.INSS / 100))
            return "Aplicando os descontos CLT..."
        else:
            return "É melhor manter o salário mínimo"

class Horista(Funcionario): # PJ não paga INSS
    def __init__(self, nome, valor=7.37, horas=220): # Valor por cada hora trabalhada e todas as horas trabalhadas no mês
        self.sal_bruto = valor*horas
        super().__init__(nome, int(self.sal_bruto))
        self.valor_hora = valor
        self.horas_trab = horas
        print(f"O(a) {type(self).__name__}(a) {self.nome} trabalha no modelo PJ")

    def calc_sal(self):
        if self.sal_bruto > Funcionario.SAL_MIN:
            self.sal_liq = self.sal_bruto
            return "Compensa continuar"
        else:
            return "É melhor trocar para o salário mínimo"


f1 = Horista("Paulo", 12, 200) # PJ
print(f1.analisar_sal())

f2 = Mensalista("Amanda", 9500) # CLT
print(f2.analisar_sal())

f3 = Mensalista("José da Silva", 8500)
print(f3.analisar_sal())

f4 = Horista("Maria de Souza", 25, 250)
print(f4.analisar_sal())