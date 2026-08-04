# Override (sobreposição)
class Mae():
    def __init__(self, nome:str):
        self.nome = nome

    def fazer_pudim(self):
        print(f"{self.nome} é {self.__class__.__name__} e está fazendo pudim")

    def fritar_coxinha(self):
        print(f"{self.nome} é {self.__class__.__name__} e está fritando coxinha")


class Filha(Mae):
    def __init__(self, nome:str):
        self.nome = nome

    def fritar_coxinha(self):
        print(f"{self.nome} é {self.__class__.__name__} e ainda não sabe fritar coxinha")

class Filho(Mae):
    def __init__(self, nome:str):
        self.nome = nome

    def fazer_pudim(self):
        print(f"{self.nome} é {self.__class__.__name__} e ainda não sabe fazer pudim")


m = Mae("Valdirene")
f1 = Filha("Maria")
f2 = Filho("João")

m.fritar_coxinha()
m.fazer_pudim()
f1.fritar_coxinha()
f1.fazer_pudim()
f2.fritar_coxinha()
f2.fazer_pudim()