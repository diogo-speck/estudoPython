from rich import print #quase sempre vai ter que ter
from rich.panel import Panel # classe Panel

caixa = Panel("[white]Esse aqui é um painel de exemplo", title="Painel", style="blue", width=25)
print(caixa)