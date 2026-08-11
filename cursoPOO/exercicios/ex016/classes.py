class Porta:
    def abrir(self):
        print(f"Girar a maçaneta e empurrar/puxar a {self.__class__.__name__}")

class Empresa:
    def abrir(self):
        print(f"Vá ao portal do empreendedor com toda a documentação para abrir uma {self.__class__.__name__}")

class Ovo:
    def abrir(self):
        print(f"Quebre a casca do {self.__class__.__name__}")

class CaixaDePandora:
    def abrir(self):
        raise Exception(f"Você não pode abrir a {self.__class__.__name__}")


def tentar_abrir(objeto):
    try:
        objeto.abrir()
    except Exception as e:
        print(f"Erro: {e}")