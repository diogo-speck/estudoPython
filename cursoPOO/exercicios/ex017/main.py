from classes import *

def main():
    a1 = Numero(67)
    b1 = Texto("Vuco ")
    c1 = Lista([1,"legal","."])
    d1 = Papel()
    e1 = Casa()

    #print(d1)

    tentar_dobrar(a1)
    tentar_dobrar(b1)
    tentar_dobrar(c1)
    tentar_dobrar(d1)
    tentar_dobrar(e1)

    print()

    print(a1)
    print(b1)
    print(c1)
    print(d1)
    print(e1)




if __name__ == "__main__":
    main()