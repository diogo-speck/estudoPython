# Implemente uma Classe Validador, simulando a validação de dados
from rich import print, inspect
from abc import ABC, abstractmethod

class Validador(ABC):
    """
        Classe abstrata que instancia um objeto chamado Validador
        Não possui atributos mas possui o método validar()
    """

    @abstractmethod
    def validar(self):
        pass


class User(Validador):
    """
    Restrições:
    - Entre 5 e 20 caracteres
    - Somente letras minúsculas
    - Pode números, underline, hífen, mas não pode espaço
    """
    def validar(self, user:str):
        if 5<=len(user)<=20 and (any(c.isupper() for c in user) == False) and (any(c==" " for c in user) == False):
            print("[green]Usuário Válido")
            return True
        else:
            print("[red]Usuário Inválido")
            return False


class Email(Validador):
    """
    Restrições:
    - Deve conter somente 1 único @ e ter pelo menos 1 caracter antes
    - Pode números, underline, hífen, mas não pode espaço
    - O TLD (fim do domínio) precisa ter pelo menos 2 letras depois de um .
    """
    def validar(self, email:str):
        email.lstrip("@")
        try:
            if (email.count("@") == 1) and (any(c==" " for c in email) == False) and len((email.split("@")[0]))>=1 and len((email.split("@")[1]).split(".")[1])>=2:
                print("[green]E-mail Válido")
                return True
            else:
                print("[red]E-mail Inválido")
                return False
        except:
                print("[red]E-mail Inválido")
                return False


class Senha(Validador):
    """
    Restrições:
    - Pelo menos 8 caracteres
    - Pelo menos uma letra maiúsculas e um número
    - Pelo menos um símbolo (exceto espaço)
    """
    def validar(self, senha:str):
        sim = False
        for i in range(len(senha)):
            if senha[i] in '!#$%&*+-.=?@_':
                sim = True
                break
        if 8<=len(senha) and (any(c.isupper() for c in senha) == True) and (any(c==" " for c in senha) == False) and (any(c.isdigit() for c in senha) == True) and sim:
            print("[green]Senha Válida")
            return True
        else:
            print("[red]Senha Inválida")
            return False



def validar_dado(tipo, valor):
    return tipo.validar(valor)