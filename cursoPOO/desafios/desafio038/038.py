from classes038 import *

def __main__():
    p1 = Produto("Notebook", 8_500)
    p2 = Produto("Mouse", 250)
    p3 = Produto("Fone de Ouvido", 450.35)

    print(p1)

    c1 = Carrinho()
    c2 = Carrinho()

    c1 = c1 + p1 + p3
    print(c1)
    c2 = c1 + p2
    print(c2)

if __name__ == "__main__":
    __main__()