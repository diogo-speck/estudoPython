from classes038 import *

def __main__():
    p1 = Produto("Mouse", 325)
    p2 = Produto("Teclado", 433)
    p3 = Produto("Memória 256", 1800)
    p4 = Produto("Placa de vídeo", 25999)

    print(p1)

    c1 = Carrinho()
    c2 = Carrinho()

    c1 = c1 + p1 + p3 + p4
    print(c1)
    c2 += c1 + p2
    print(c2)

if __name__ == "__main__":
    __main__()