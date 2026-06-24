# Crie a classe Livro, que vai simular a passagem de páginas de um livro, considerando também se o usuário chegou ao fim da leitura.
from rich import print

class Livro:
    """
        Classe que instancia um objeto chamado Livro e atribui a ele um título e uma quantidade n de páginas
        ex. objeto = Livro(nome, n)
        Possui um método ler() para avançar p páginas desejadas
        ex. objeto.ler(p)
    """
    def __init__(self, nome="", n=0):
        self.nome = nome
        self.n = n
        self.lido = 0
        print(f':open_book: [blue]Você acabou de abrir o livro [red]"{self.nome}"[/] que tem [green]{self.n} páginas[/] no total. Você agora está na [yellow]página {self.lido+1}')
    
    def ler(self, p=1):
        if self.lido+p>=self.n:
            restantes = self.n-self.lido
        for i in range(0, p, 1):
            if not self.fim_do_livro(): # se ainda não chegou no fim do livro
                print (f"Pág.{self.lido+1} ⏩ ", end="")
                self.lido+=1
        if self.fim_do_livro():
            print(f"\n[blue]Você leu as {restantes} páginas restantes do livro, parabéns.")
            return f':closed_book: [red]Você chegou ao final do livro "{self.nome}" com {self.n} páginas'
        else:
            return f"\n[blue]Você leu {p} páginas, parabéns. Agora você está na [yellow]página {self.lido+1}"
            
    def fim_do_livro(self):
        return True if self.lido == self.n else False

nome = input("Qual o nome do livro que você deseja ler? ")
paginas = int(input(f"Qual a quantidade de páginas do livro \"{nome}\"? "))
l1 = Livro(nome, paginas)

while l1.lido < paginas:
    qtd = int(input("Quantas páginas você deseja ler? "))
    print(l1.ler(qtd))