from Credencial030 import *

def __main__():
    c1 = Credencial("Diogo")
    inspect(c1, private=True, methods=True)

    print("Hash:", c1.hash)
    print("Cifra:", c1.cifra)
    print("Validação correta:", c1.validar("Diogo"))  # True
    print("Validação errada:", c1.validar("123"))     # False

    cripto = input("Digite algo para ser criptografado: ")
    c2 = Credencial(cripto)
    print("Seu texto criptografado:")
    print(c2.hash)

if __name__ == "__main__":
    __main__()