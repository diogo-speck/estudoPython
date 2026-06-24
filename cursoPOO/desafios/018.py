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
    consumo_padrao:float = 0.4 # 400 gramas por pessoa em média
    preco_kg:float = 82.4 # R$82,40 em média cada kg de carne

    def __init__(self, n=0):
        self.n = n
    def __str__(self):
        carne = self.n*Churrasco.consumo_padrao
        preco = carne*Churrasco.preco_kg
        return f'\nVão participar do churrasco [green]"{festa}"[/] [blue]{self.n} pessoas[/], para isso deve ser comprado uns [blue]{carne:,.1f}kg[/] de carne, custando em média [green]R${preco:,.2f}[/] ou aproximadamente [yellow]R${(preco/self.n):,.2f}[/] por pessoa\n'

linhas = f"{"-".center(104, '-')}" # cabiam 100 caracteres no terminal, mas o panel usa mais 4, 2 de cada lado
print(linhas)
festa = input("Qual o nome da resenha? ")
p = int(input("Quantas pessoas vão? "))
c1 = (Churrasco(p)) # Churrasco para p pessoas
festa = Panel(f"{linhas}{str(c1)}{linhas}", title=festa) # precisar passar o objeto para String
print(festa)