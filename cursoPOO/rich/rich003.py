from rich import print
from rich.table import Table

tabela = Table(title="Preços Mercado")
tabela.add_column("Item", justify="left", style="yellow")
tabela.add_column("Preço/kg", justify="center", style="green")

tabela.add_row("Banana", "R$1,99")
tabela.add_row("Batata", "R$2,99")
tabela.add_row("Caqui", "R$4,99")

print(tabela)