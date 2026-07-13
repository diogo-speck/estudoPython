# Implemente uma Classe Diario, onde vamos simular o funcionamento de um diário secreto com senha
from rich import print, inspect
from rich.panel import Panel

class Diario:
    """
        Classe que instancia um objeto chamado Diario que inicia aberto sem senha, além disso, cria uma lista com os segredos
        ex. d1 = Diario()
        Possui 2 métodos:
        escrever(msg)
        ex. d1.escrever("Testando")
        escreve no diário
        ex. d1.ler()
        lê tudo no diário se usar a senha correta
    """

    def __init__(self, senha=""):
        self.__segredos = []
        self.__senha = senha

    def escrever(self, msg):
        self.__segredos.append(msg)
        print(f"Mensagem escrita")

    def ler(self, senha=""):
        if senha == self.__senha:
            texto = ""
            for segredo in self.__segredos:
                texto+=f"{segredo}"
            return texto
        else:
            return f"Senha incorreta"


d1 = Diario("123")

d1.escrever("Bem-Vindo ao diário\n")
d1.escrever("Aqui o segredo é secreto")

print(d1.ler())
print(d1.ler("1234"))
print(d1.ler("123"))