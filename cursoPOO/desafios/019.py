# Crie a classe Livro, que vai simular a passagem de páginas de um livro, considerando também se o usuário chegou ao fim da leitura.
# Minuto 11 aula 06
class Livro:
    def __init__(self, nome="", n=0):
        self.nome = nome
        self.n = n
        self.lido = 0
        print(f'Você acabou de abrir o livro "{self.nome}" que tem {self.n} páginas no total.')
    def ler(self, p):
        for i in range(self.lido+1, self.lido+p+1):
            if self.lido+p<=self.n:
                print (f"Pág. {i} lida ") # tem que arrumar
                self.lido+=p
                return f"Você leu {p} páginas, parabéns. Agora você está na página {self.lido}"
            else:
                self.lido = self.n
                return f"Você terminou de ler o livro {self.nome} com {self.n} páginas"
        
        

nome = input("Qual o nome do livro que você deseja ler? ")
paginas = int(input(f"Qual a quantidade de páginas do livro {nome}? "))
l1 = Livro(nome, paginas)

while l1.lido < paginas:
    qtd = int(input("Quantas páginas você deseja ler? "))
    print(l1.ler(qtd))