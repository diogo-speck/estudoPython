# Crie a classe Produto, onde podemos cadastrar nome e o preço. Crie também um método que mostre uma etiqueta de preço do produto.
from rich import print
from rich.table import Table

class Produto:
    """
        Classe que instancia um objeto chamado Produto e atribui a ele um nome e um preço
        ex. objeto = funcionario("nome", preço)
        Possui um método de etiqueta para mostrar todas os atributos
        ex. objeto.etiqueta()
    """
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    def etiqueta(self):
        etiqueta.add_row(f"{self.nome}", f"R${self.preco}")
        print(etiqueta)

etiqueta = Table(title="Etiquetas")
etiqueta.add_column("Produtos")
etiqueta.add_column("Preços")

p1 = Produto("iPhone 17 Pro Max", 25_000.85)
p2 = Produto("Notebook Gamer", 8_000.00)

p1.etiqueta()
p2.etiqueta()