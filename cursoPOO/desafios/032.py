# Exercício Conta Bancária (ex006) Aprimorado

import random
from Credencial030 import Credencial, print, inspect

class ContaBancaria(Credencial):
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

    def __init__(self, nome, senha="senh@123", saldo=0):
        super().__init__(senha)
        self._nome = nome
        self._id = str(random.randint(1, 999)).zfill(3)
        self.__saldo = saldo

        print(f"Conta {self._id} criada no nome de {self._nome}. Saldo atual R${self.__saldo:,.2f}")

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        print("Para mudar de nome, confirme que é você mesmo")
        if self.pede_senha():
            self._nome = nome
            print(f"O novo nome do titular agora é {self._nome}")
        else:
            print(f"Senha inválida! Não foi possível mudar o nome do titular ({self._nome})")

    def validar_senha(self, chave):
        return super().validar(chave)

    def pede_senha(self, chave=""):
        if chave == "":
            senha = input("Digite sua senha: ")
        else:
            senha = chave
        return self.validar_senha(senha)


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
        return f"{self._nome} é o titular da conta {self._id}, seu saldo atual é de R${self.__saldo:,.2f}"



c1 = ContaBancaria("Maria", "maria123")
c1.depositar(-500)
c1.sacar(-100, "senha")
c1.sacar(500, "maria123")
print()
c2 = ContaBancaria("Gustavo", "gafanhoto", 1000)
c2.depositar(500)
c2.sacar(200)
c2.nome = "Manoel"
#inspect(c2)