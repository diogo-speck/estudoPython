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
        print(f'Você acabou de abrir o livro "{self.nome}" que tem {self.n} páginas no total.')
    def ler(self, p):
        if (self.lido+p>=self.n):
            self.lido=self.n
            for i in range(self.n):
                print (f"Pág.{i+1} ⏩ ", end="")
            return f"Você chegou ao final do livro {self.nome} com {self.n} páginas"
        else:
            for i in range(p):
                print (f"Pág.{self.lido+i+1} ⏩ ", end="")
            self.lido+=p
            return f"\nVocê leu {p} páginas, parabéns. Agora você está na página {self.lido}"


nome = input("Qual o nome do livro que você deseja ler? ")
paginas = int(input(f"Qual a quantidade de páginas do livro {nome}? "))
l1 = Livro(nome, paginas)

while l1.lido < paginas:
    qtd = int(input("Quantas páginas você deseja ler? "))
    print(l1.ler(qtd))