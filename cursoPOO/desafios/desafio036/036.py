from classes036 import *

def __main__():
    finalizar_compra(Boleto(), -8_500)
    finalizar_compra(Pix(), 324.20)
    finalizar_compra(Cartao(), 1_500)

if __name__ == "__main__":
    __main__()