# Crie uma classe Funcionario, onde podemos cadastrar nome, setor e cargo. Crie também um método que permitaao funcionário se apresentar.
from rich import print
from rich import inspect

class Funcionario:
    """
        Classe que instancia um objeto chamado Funcionario e atribui a ele um nome, um setor e um cargo
        ex. objeto = funcionario("nome", "setor", "cargo")
        Possui um método de apresentação para mostrar todas os atributos
        ex. print(objeto.apresentar())
    """
    # Atributos de Classe (não precisa de self)
    empresa = "Curso em Vídeo"

    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentar(self):
        apresentacao = f"[blue]{self.nome}[white] é funcionário(a) que trabalha como {self.cargo} no setor de {self.setor} da empresa {Funcionario.empresa} :+1:" # ou self.__class__.empresa
        return apresentacao


# inspect(Funcionario)
Funcionario.empresa = "Diogo's Corporation"
f1 = Funcionario("Mário", "manutenção", "encanador")
print(f1.apresentar())
f2 = Funcionario("Maria", "administração", "diretora")
f2.empresa = "SESC" # não muda a classe, só cria um atributo do objeto f2 mas classe têm prioridade
print(f2.apresentar())
f3 = Funcionario("Pedro", "TI", "programador")
print(f3.apresentar())
# inspect(f2, methods=True)