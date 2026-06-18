# Declaração de Classe (Molde)
class Gafanhoto:
    """
        Manual da Classe:
        Essa classe cria um Gafanhoto, que é uma pessoa que tem nome e idade.
        Para criar uma nova pessoa (objeto), use:
        variavel = Gafanhoto("nome", idade)
    """
    def __init__(self, nome = "", idade = 0): # Método Construtor / Por padrão se não receber nada atribui os parâmetros nenhum nome e idade 0
        # Atributos de Instância (dados)
        self.nome = nome
        self.idade = idade

    # Métodos de Instâncias
    def aniversario(self): # Objeto chamado, no caso g1
        self.idade = self.idade+1 # self é a maneira genérica de chamar o próprio objeto

    def parabens(self): # Deseja parabéns por fazer aniversário
        return f"{self.nome} fez aniversário e agora tem {self.idade} anos de idade."
    
    def __str__(self): #Dunder Method
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} ano(s) de idade."
    
    def __getstate__(self):
        if self.nome == "": # se não tiver nome
            return "Sem CPF"
        else:
            return ""

# Declaração de Objetos (Biscoito)
g1 = Gafanhoto("Diogo", 18) # Objeto sendo instânciando por uma chamada do método contrutor
print(g1) # Normalmente printaria o endereço de memória, mas usando __str__, agora printa uma mensagem
# g1.nome = "Diogo"
# g1.idade = 18 Atributos não usa ()
g1.aniversario() # Método usa () chamando o objeto g1
print(g1.parabens())
print(g1.__getstate__())

g2 = Gafanhoto("Xuxa", 63)
print(g2)
# g2.nome = "Xuxa"
# g2.idade = 63
g2.aniversario()
print(g2.parabens())
print(g2.__getstate__())

# Só posso usar métodos depois de criar o objeto, ex. não poderia usar o g3.aniversario() antes do g3 = Gafanhoto()
g3 = Gafanhoto()
# print(g3)
print(g3.__dict__) # Dunder Attribute (não modificável)
print(g3.__getstate__()) # Dunder Method (modificável)

print()
print(g1.__doc__) # Testando a DocString da classe
# print(int.__doc__) DUNDER = Double Underline __
# print(g1.__class__) Mostra a classe do objeto (<class '__main__.Gafanhoto'>)

# Todo atributo tem valores de um estado