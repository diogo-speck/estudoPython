# Implemente uma Classe Carrinho, simulando um carrinho de compras

class Carrinho():
    """
        Classe que instancia um objeto chamado Carrinho onde recebe produtos e calcula um total
        OBS: estrutura com agregacao, incluindo sobrecarga do operador + para adicionar produtos ao carrinho de compras
        Possui os atributos +produtos (público) e @total (público)
        ex. c1 = Carrinho()
    """

    def __init__(self):
        self.produtos = []
        self._total = 0.0

    def __iadd__ (self, produto):
        self.produtos.append(produto)
        self._total += (produto._valor)
        return self

    def __str__(self):
        sacola = ""
        for i in self.produtos:
             sacola+=f"{i}\n"
        return f"\n{sacola}\nTotal: R$ {self._total:,.2f}"

class Produto():
    def __init__(self, item, valor=0.0):
            self.item = item
            self._valor = valor

    def __str__(self):
         return f"{self.item} (R$ {self._valor:,.2f})"