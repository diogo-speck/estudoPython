# Crie a Classe Gamer, onde podemos cadastrar nome, nick, e os jogos favoritos de uma pessoa. Crie também um método que permita mostrar a ficha desse gamer.
from rich import print
from rich.panel import Panel
class Gamer:
    """
        Classe que instancia um objeto chamado Gamer e atribui a ele um nome, nick e os jogos favoritos de uma pessoa
        ex. objeto = Gamer("nome", "nick")
        Possui 2 métodos: add_favoritos() para adicionar jogos a uma lista;
        ex. objeto.add_favoritos("jogo")
        ficha() para printar todos os atributos
        ex. print(objeto.ficha())
    """
    def __init__(self, nome, nick, jogos=[]):
        self.nome = nome
        self.nick = nick
        self.jogos = list()

    def ficha(self):
        conteudo = f"Nome real: [black on blue] {self.nome} [/]\nJogos Favoritos: [blue]"
        for num, jogo in enumerate(self.jogos): # só a parte do jogo da tupla
            conteudo+= f"\n :video_game: {jogo}"
        return Panel(conteudo, title=f"Jogador <{self.nick}>", width=35)
    
    def add_favoritos(self, jogo):
        self.jogos.append(jogo)
        self.jogos.sort()

j1 = Gamer("Fabrício da Silva", "detonator2025")
j1.add_favoritos("Mario Bros")
j1.add_favoritos("Sonic")
j1.add_favoritos("God of War")
j1.add_favoritos("Fortnite")
print(j1.ficha())

j2 = Gamer("Olívia Souza", "peach_raivosa")
j2.add_favoritos("Mario Bros")
j2.add_favoritos("Call of Duty")
print(j2.ficha())