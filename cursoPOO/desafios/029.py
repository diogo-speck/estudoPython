# Implemente uma Classe Diario, onde vamos simular o funcionamento de um diário secreto com senha
from rich import print, inspect

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
        self.__senha = senha.strip()

    @property
    def senha(self):
        raise PermissionError("Ninguém tem permissão para ver a senha")

    @senha.setter
    def senha(self, senha= None):
        if senha == self.__senha:
            print("[green]Senha Correta - Liberado ✅ [/]")
            nsenha = input("Digite sua nova senha: ")
            self.__senha = nsenha
        else:
            print("Não foi possível mudar sua senha")
            raise PermissionError("Senha incorreta")

    def escrever(self, msg):
        if isinstance(msg, str) and len(msg) > 0:
            self.__segredos.append(msg)
            print(f"Mensagem escrita")
        else:
            print(f"Mensagem inválida")

    def ler(self, senha=""):
        if senha == self.__senha:
            texto = "[green]Senha Correta - Liberado ✅ [/] \n\n"
            for segredo in self.__segredos:
                texto+=f"{segredo}"
            return texto
        else:
            raise PermissionError("Senha incorreta")


d1 = Diario("123")

d1.escrever("Bem-Vindo ao diário\n")
d1.escrever("Aqui o segredo é secreto")
try:
    print(d1.ler("123"))
except PermissionError as e:
    print(f"[red]Erro: {e}")
try:
    d1.senha = "123"
except PermissionError as e:
    print(f"[red]Erro: {e}")

inspect(d1, private=True, methods=True)