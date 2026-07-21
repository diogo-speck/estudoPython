# Exercício Conta Bancária (ex006) Aprimorado com hash sha256

from Criptografia032 import *


def main():
    c1 = ContaBancaria(111, nome="Josenildo", saldo=10_000, senha="Guanabara")
    c1.sacar(500)
    c1.nome = "Maricota"
    #inspect(c1, private=True, methods=True)


if __name__ == "__main__":
    main()