# Implemente uma Classe Carrinho, simulando um carrinho de compras com agregação incluindo sobrecarga de operador

class Carrinho():
    """
        Classe que instancia um objeto chamado Carrinho onde recebe produtos e calcula um total
        OBS: estrutura com agregacao, incluindo sobrecarga do operador + para adicionar produtos ao carrinho de compras
        Possui os atributos +produtos (público) e @total (público)
        ex. c1 = Carrinho()
    """

    def __init__(self, produtos:list=None):
        self.produtos = produtos if produtos else []

    @property
    def total(self):
         return sum(p._valor for p in self.produtos)

    def __add__ (self, produto):
        if isinstance(produto, Produto):
            return Carrinho(self.produtos + [produto])
        elif isinstance(produto, Carrinho):
            return Carrinho(self.produtos + [produto.produtos])
        else:
            raise TypeError("Você tentou adicionar algo inválido ao carrinho")

    def __str__(self):
        linha = "\n" + "-" * 30 + "\n"
        itens = "\n".join(str(p) for p in self.produtos)
        return f"\n{linha}{itens}{linha}Total: {formataDinheiro(self.total)}"


class Produto():
    def __init__(self, item:str, valor:float=0.0):
            self.item = item
            self._valor = valor

    def __str__(self):
         return f"{self.item} ({formataDinheiro(self._valor)})"



def formataDinheiro(valor:float):
    import locale
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    return locale.currency(valor, grouping=True)