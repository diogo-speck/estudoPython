from classes035 import *

def __main__():
    a1 = DOCX("prova", 250_000)
    a2 = PDF("contrato", 1_300_000)
    a3 = PNG("logo", 1_200_000)
    a4 = JPEG("foto", 300_000)
    a5 = GIF("loaf_cat", 500_000)

    a1.abrir()
    a2.abrir()
    a3.abrir()
    a4.abrir()
    a5.abrir()

if __name__ == "__main__":
    __main__()