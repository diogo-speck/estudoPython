"""import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from desafios.desafio040.classes040 import *

#gambiarra"""
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


    exportar_dados(JSON(), a)
    exportar_dados(XML(), u)


if __name__ == "__main__":
    __main__()