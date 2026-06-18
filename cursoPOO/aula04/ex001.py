# Declaração de Classe (Molde)
class Gafanhoto:
    def __init__(self): # Método Construtor
        # Atributos de Instância (dados)
        self.nome = ""
        self.idade = 0

    # Métodos de Instâncias
    def aniversario(self): # Objeto chamado, no caso g1
        self.idade = self.idade+1 # self é a maneira genérica de chamar o próprio objeto

    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."

# Declaração de Objetos (Biscoito)
g1 = Gafanhoto() # Objeto sendo instânciando por uma chamada do método contrutor
g1.nome = "Diogo"
g1.idade = 18 # Atributos não usa ()
g1.aniversario() # Método usa () chamando o objeto g1
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = "Xuxa"
g2.idade = 63
g2.aniversario()
print(g2.mensagem())

# Só posso usar métodos depois de criar o objeto, ex. não poderia usar o g3.aniversario() antes do g3 = Gafanhoto()
g3 = Gafanhoto()
g3.aniversario()
print(g3.mensagem())

# Todo atributo tem valores de um estado