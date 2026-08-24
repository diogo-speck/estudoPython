from desafios.desafio040.classes040 import *

def __main__():
    
    u = [
        Login("Pedro", "pedro@gmail.com"),
        Login("Mariazinha", "Mariazinha@hotmail.com")
    ]

    a = [
        Estudante("Claúdia", 'ADS', "2 per"),
        Estudante("Ana", "ADM", "4 per"),
        Estudante("Mario", "SEG", "1 per")
    ]

    print(u)
    print(a)


    # exportar_dados(JSON(), u)

if __name__ == "__main__":
    __main__()