# Aprimore o exercicio da ContaBancaria (ex.006), aplicando conceitos de encapsulamento
from rich import print, inspect
import random, string
from hashlib import sha256

class Criptografia:
    """
        Classe que instancia um objeto chamado Criptografia onde recebe uma 'String' e devolve outra criptografada com hash sha256
        Possui o atributo @hash (público)
        ex. c1 = Criptografia("senha")
        Possui 1 method:
        validar(senha)
        ex. c1.validar("123")
    """

    def __init__(self, senha):
        self.__hash = self.__criptografar(senha)


    def __criptografar(self, texto):
        cripto = sha256((texto.strip()).encode('utf-8')).hexdigest()
        return cripto

    def validar(self, senha):
        return self.__criptografar(senha.strip()) == self.__hash


class ContaBancaria(Criptografia):
    """
        Classe que instância um objeto chamado ContaBancaria que permite 'id', titular, saldo, nome de quem fez a
        transação e o hash/senha de transferência
        Possui 4 métodos, sendo eles:
        validar_senha(chave) semelhante ao exemplo da credencial, ocultando a senha e verificando
        ex. validar_senha(chave)
        pede_senha() pede para o utilizador digitar a senha
        ex. pede_senha()
        depositar(valor) valores positivos
        ex. depositar(valor)
        sacar(valor, chave) só pode sacar valores possíveis em conta
        ex. sacar(valor, chave)
    """

    def __init__(self, id=None, nome=None, senha:str=None, saldo:float=0):
        if senha is None:
            super().__init__(self.pede_senha())
        else:
            super().__init__(senha)
        if id is None:
            id=random.randint(1, 999)
        self._id = str(id).zfill(3)
        self._nome = None
        self.nome = nome
        self.__saldo = saldo

        print(f"Conta {self._id} criada no nome de {self._nome}. Saldo atual R${self.__saldo:,.2f}")

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome=None):
        if self._nome is None:
            self._nome = nome
            while self._nome is None or len(self._nome.strip())<2:
                print("Nome não registrado ou inválido")
                self._nome = input("Digite seu nome: ")
            print(f"O novo nome do(a) titular agora é {self._nome}")
        else:
            print("Para mudar de nome, confirme que é você mesmo")
            if self.pede_senha(""):
                self._nome = nome
                while self._nome is None or len(self._nome.strip())<2:
                    print("Nome inválido")
                    self._nome = input("Digite seu nome: ")
                print(f"O novo nome do(a) titular agora é {self._nome}")
            else:
                print(f"Senha inválida! Não foi possível mudar o nome do(a) titular ({self._nome})")

    def validar_senha(self, chave):
        return super().validar(chave)

    def pede_senha(self, chave=None):

        from pwinput import pwinput # Funciona somente dentro da função

        if chave is None:
            return pwinput("Crie uma senha: ")

        if chave == "":
            chave = pwinput("Digite sua senha: ")

        return self.validar_senha(chave)


    def depositar(self, valor):
        valor = abs(valor)
        self.__saldo += valor
        print(
            f"{self._nome} recebeu R${valor:,.2f} em sua conta {self._id} e agora tem R${self.__saldo:,.2f} de saldo")

    def sacar(self, valor, chave=""):
        valor = abs(valor)
        print(f"Você escolheu sacar R${valor:,.2f} da conta {self._id} de {self._nome}")
        if self.pede_senha(chave):
            if valor > self.__saldo:
                print(
                    f"Saldo insuficiente em sua conta {self._id} {self._nome}, faça um depósito de pelo menos R${(valor - self.__saldo):,.2f}")
            else:
                self.__saldo -= valor
                print(
                    f"{self._nome} sacou R${valor:,.2f} em sua conta {self._id} e agora tem R${self.__saldo:,.2f} de saldo")
        else:
            print("Senha inválida! Não foi possível fazer o saque")

    def __str__(self):
        return f"{self._nome} é o(a) titular da conta {self._id}, seu saldo atual é de R${self.__saldo:,.2f}"