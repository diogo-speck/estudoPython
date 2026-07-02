from abc import ABC, abstractmethod # Abstract Base Classes

class Pessoa(ABC): # SuperClasse Abstrata
    """
        SuperClasse chamado Pessoa em uma academia abstrata que possui os parâmetros nome, idade e lista de alunos matriculados
        ex. e1 = Pessoa()
        Possui os métodos fazerAniversário():
        ex. e1.fazerAniversário()
    """
    alunos = []
    def __init__(self, nome="", idade=0):
        self.nome = nome
        self.idade = idade
    
    def fazerAniversario(self):
        self.idade+=1

    @abstractmethod # Métodos Obrigatórios
    def estaNaAcademia(self):
        pass

class Aluno(Pessoa): # SubClasse
    """
        SubClasse derivada da Class Pessoa, que instancia um objeto chamado Aluno e atribui a ele um nome e idade
        (da super classe), além disso também dá a ele um treino, um dia da semana e inicializa-o como não-matriculado
        ex. a1 = Aluno("nome", idade, "treino", "dia")
        Possui 2 métodos, os métodos fazerAniversário() da classe Pessoa:
        ex. a1.fazerAniversário()
        E os métodos fazerMatricula():
        ex. print(a1.fazerMatricula())
    """
    def __init__(self, nome="", idade=0, treino="A", dia=""):
        super().__init__(nome, idade)
        self.treino = treino
        self.dia = dia
        self.matriculado = False

    def fazerMatricula(self):
        if self.matriculado:
            return f"O(a) aluno(a) [green]{self.nome}[/] já está matriculado"
        else:
            self.matriculado = True
            Pessoa.alunos.append(self.nome)
            return f"O(a) aluno(a) [green]{self.nome}[/] foi matriculado"

    def malhar(self, treinoatual="", diaatual=""):
        if treinoatual == "":
            treinoatual = self.treino
        if diaatual == "":
            diaatual = self.dia
        print(f"O último treino do(a) {self.nome} foi {self.treino} na(o) {self.dia}")
        self.treino, self.dia = treinoatual, diaatual
        return f"Hoje é [blue]{diaatual}[/] e seu treino é [red]{treinoatual}"

    def estaNaAcademia(self):
        return f"O(a) aluno(a) {self.nome} está na academia treinando {self.treino} na {self.dia}"


class Professor(Pessoa): # SubClasse
    """
        SubClasse derivada da Class Pessoa, que instancia um objeto chamado Professor/instrutor e atribui a ele um
        nome e idade (da super classe), além disso também dá a ele um tipo de aula ex. funcional e um nível
        (por padrão superior que é o mínimo para dar aula no Brasil)
        ex. p1 = Professor("nome", idade, "tipo", "nivel")
        Possui 2 métodos, os métodos fazerAniversário() da classe Pessoa:
        ex. p1.fazerAniversário()
        E os métodos darAula():
        ex. print(p1.darAula())
    """
    def __init__(self, nome="", idade=0, tipo="musculação", nivel="superior"):
        super().__init__(nome, idade)
        self.tipo = tipo
        self.nivel = nivel

    def darAula(self):
        return f"O(a) professor(a) [black on white]{self.nome}[/] começou a dar aula de [orange]{self.tipo}[/] para o(s) aluno(s): {Aluno.alunos}"

    def estaNaAcademia(self):
        return f"O(a) instrutor(a) {self.nome} de nível {self.nivel} está na academia dando aula de {self.tipo}"


class Funcionario(Pessoa): # SubClasse
    """
        SubClasse derivada da Class Pessoa, que instancia um objeto chamado Funcionário e atribui a ele um nome e idade
        (da super classe), além disso também dá a ele um cargo, um setor e inicializa-o com o ponto não-batido
        ex. f1 = Funcionario("nome", idade, "cargo", "setor")
        Possui 3 métodos, os métodos fazerAniversário() da classe Pessoa:
        ex. f1.fazerAniversário()
        Os métodos baterPonto():
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
            return f"O(a) funcionário(a) [purple]{self.nome}[/] já bateu o ponto"
        else:
            self.pontoBatido = True
            return f"O(a) funcionário(a) [purple]{self.nome}[/] bateu o ponto"
    
    def __str__(self):
        if self.pontoBatido:
            return f"O(a) funcionário(a) {self.nome} está trabalhando no setor de {self.setor} como {self.cargo}"
        else:
            return f"O(a) funcionário(a) {self.nome} ainda não bateu o ponto"

    def estaNaAcademia(self):
        return f"O(a) funcionário(a) {self.nome} do setor de {self.setor} está na academia trabalhando como {self.cargo}"