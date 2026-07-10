from rich import print, inspect
from ex006 import *

def main():
    c1 = Conta("Maria", 111, 5_000)
    c1.deposito(-500)
    c1.saque(-100)
    #c1._Conta__saldo = 0 Pode alterar, mas não deve
    print(c1.__dict__)

if __name__ == "__main__": # boa prática para arquivos maiores e se quiser mudar o nome
    main()