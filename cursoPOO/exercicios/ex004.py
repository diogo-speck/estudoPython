from rich import print, inspect

class Pessoa: # SuperClasse
    """
        SuperClasse que instancia um objeto chamado Pessoa e atribui a ele um nome, idade e a lista de alunos matriculados
        ex. e1 = Pessoa()
        Possui o método fazerAniversário(): 
        ex. e1.fazerAniversário()
    """
    alunos = []
    def __init__(self, nome="", idade=0):
        self.nome = nome
        self.idade = idade
    
    def fazerAniversario(self):
        self.idade+=1
    

class Aluno(Pessoa): # SubClasse
    """
        SubClasse derivada da Class Pessoa, que instancia um objeto chamado Aluno e atribui a ele um nome e idade (da super classe), além disso também dá a ele um curso, turma e inicializa-o como não-matriculado
        ex. a1 = Aluno("nome", idade, "curso", "turma")
        Possui 2 métodos, o método fazerAniversário() da classe Pessoa: 
        ex. a1.fazerAniversário()
        E o método fazerMatricula():
        ex. print(a1.fazerMatricula())
    """
    def __init__(self, nome="", idade=0, curso="", turma=""):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma
        self.matriculado = False

    def fazerMatricula(self):
        if self.matriculado:
            return f"O aluno {self.nome} já está matriculado"
        else:
            self.matriculado = True
            Pessoa.alunos.append(self.nome)
            return f"O aluno {self.nome} foi matriculado"
        


class Professor(Pessoa): # SubClasse
    """
        SubClasse derivada da Class Pessoa, que instancia um objeto chamado Professor e atribui a ele um nome e idade (da super classe), além disso também dá a ele uma especialidade e um nível (por padrão superior que é o mínimo para dar aula no Brasil)
        ex. p1 = Professor("nome", idade, "especialidade", "nivel")
        Possui 2 métodos, o método fazerAniversário() da classe Pessoa: 
        ex. p1.fazerAniversário()
        E o método darAula():
        ex. print(p1.darAula())
    """
    def __init__(self, nome="", idade=0, especialidade="", nivel="superior"):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def darAula(self):
        return f"O professor(a) {self.nome} começou a dar aula de {self.especialidade} para o(s) aluno(s) {Aluno.alunos}"


class Funcionario(Pessoa): # SubClasse
    """
        SubClasse derivada da Class Pessoa, que instancia um objeto chamado Funcionário e atribui a ele um nome e idade (da super classe), além disso também dá a ele um cargo, um setor e inicializa-o com o ponto não-batido
        ex. f1 = Funcionario("nome", idade, "cargo", "setor")
        Possui 3 métodos, o método fazerAniversário() da classe Pessoa: 
        ex. f1.fazerAniversário()
        O método baterPonto():
        ex. print(f1.baterPonto())
        E o dunder method __str__ para mostrar os atributos e o estado atual do funcionário:
        ex. print(f1)
    """
    def __init__(self, nome="", idade=0, cargo="", setor=""):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor
        self.pontoBatido = False

    def baterPonto(self):
        if self.pontoBatido:
            return f"O(a) funcionário(a) {self.nome} já bateu o ponto"
        else:
            self.pontoBatido = True
            return f"O(a) funcionário(a) {self.nome} bateu o ponto"
    
    def __str__(self):
        if self.pontoBatido:
            return f"O(a) funcionário(a) {self.nome} está trabalhando no setor de {self.setor} como {self.cargo}"
        else:
            return f"O(a) funcionário(a) {self.nome} ainda não bateu o ponto"


a1 = Aluno("José", 17, "informática", "T01")
a1.fazerAniversario()
print(a1.fazerMatricula())
print(a1.fazerMatricula())
# inspect(a1, methods=True) equivalente a (a1.__dict__)

p1 = Professor("Samuel", 37, "biologia", "mestre")
p1.fazerAniversario()
print(p1.darAula())
# inspect(p1, methods=True)

f1 = Funcionario("Claúdia", 27, "secretária escolar", "secretaria")
print(f1)
f1.fazerAniversario()
print(f1.baterPonto())
print(f1.baterPonto())
print(f1)
# inspect(f1, methods=True)