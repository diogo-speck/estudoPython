class Numero:
    def __init__(self, valor:int|float=0):
        self.valor = valor

    def dobrar(self):
        self.valor *= 2
        print(f"Seu {self.__class__.__name__} dobrado: {self.valor}")

    def __str__(self):
        return f'Valor armazenado = {self.valor}'

class Texto:
    def __init__(self, texto:str=""):
        self.texto = texto

    def dobrar(self):
        self.texto *= 2
        print(f'Seu novo {self.__class__.__name__} dobrado: {self.texto}')

    def __str__(self):
        return f'Texto armazenado = "{self.texto}"'

class Lista:
    def __init__(self, lista:list|tuple|dict=[]):
        self.lista = lista

    def dobrar(self):
        dobrado = [c*2 for c in self.lista]
        self.lista = dobrado
        print(f"Sua nova {self.__class__.__name__} dobrada: {self.lista}")

    def __str__(self):
        return f'Lista armazenada = "{self.lista}"'

class Papel:
    def __init__(self):
        self.dobrado = False

    def dobrar(self):
        print(f"Você pode dobrar um {self.__class__.__name__}")
        self.dobrado = True

    def __str__(self):
        return f'O {self.__class__.__name__} {"não " if not self.dobrado else ""}está dobrado'

class Casa:
    def dobrar(self):
        raise Exception(f"Você não pode dobrar uma {self.__class__.__name__}")

    def __str__(self):
        return f'A casa está inteira'


def tentar_dobrar(objeto):
    try:
        objeto.dobrar()
    except Exception as e:
        print(f"Erro: {e}")