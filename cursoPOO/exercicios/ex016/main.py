from classes import *

def main():
    a1 = Porta()
    a2 = Empresa()
    a3 = Ovo()
    a4 = CaixaDePandora()

    #Duck Typing - Não importa a classe, o que importa é que ela funciona
    tentar_abrir(a1)
    tentar_abrir(a2)
    tentar_abrir(a3)
    tentar_abrir(a4)




if __name__ == "__main__":
    main()