from rich import print, inspect
from ex007a010 import *

def main():
    av1 = Avaliacao("Pedro","Matemática")
    #print(av1.get_nota())
    #av1.set_nota(10)
    av1.nota = 7 # parecido como se fosse trocar diretamente um atributo
    print(av1)
    av1.set_nota(-5)

if __name__ == "__main__":
    main()