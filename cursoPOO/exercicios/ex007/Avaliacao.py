from rich import print, inspect
from ex007 import *

def main():
    av1 = Avaliacao("Pedro","Matemática")
    print(av1.get_nota())
    av1.set_nota(10)
    print(av1)
    av1.set_nota(-5)

if __name__ == "__main__": # boa prática para arquivos maiores e se quiser mudar o nome
    main()