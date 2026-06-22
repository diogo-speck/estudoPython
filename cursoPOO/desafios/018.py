# Crie a classe Churrasco, onde seja possível informar quantas pessoas vão participar e mostre quanto de carne deve ser comprado, o custo total do churrasco e o preço por pessoa.
from rich import print
from rich.panel import Panel

class Churrasco:
    """
        Classe que instancia um objeto chamado Churrasco e atribui a ele uma quantidade n de pessoas
        ex. objeto = Churrasco(n)
        Possui um Dunder method String para printar os dados desejados
        ex. print(objeto)
    """
    def __init__(self, n=0):
        self.n = n
    def __str__(self):
        carne = self.n*0.4 # 400 gramas por pessoa em média
        preco = carne*82.4 # R$82,40 em média cada kg de carne
        return f"Vão participar do churrasco {self.n} pessoas, para isso deve ser comprado uns {carne:,.1f} kg de carne, custando em média R${preco:,.2f} ou aproximadamente R${(preco/self.n):,.2f} por pessoa"

festa = input("Qual o nome da resenha? ")
p = int(input("Quantas pessoas vão? "))
c1 = (Churrasco(p)) # Churrasco para p pessoas
festa = Panel(str(c1), title=festa) # precisar passar o objeto para String
print(festa)