# Implemente uma Classe Retangulo, simulando um retângulo com as suas medidas e área
from rich import print, inspect

class Retangulo:
    """
        Classe que instancia um objeto chamado Retangulo onde recebe uma base e altura
        Possui os atributos _base (protegido) / @base (encapsulado e validado), _altura/@altura, _area/@area e @medidas
        ex. c1 = Retangulo("senha")
        Possui 1 method:
        validar(senha)
        ex. c1.validar("123")
    """
    def __init__(self, base=0, altura=0):
        self._base = base
        self._altura = altura
        self._area = self._base * self._altura
        self._medidas = None

    @property
    def base(self):
        return self._base
    @property
    def altura(self):
        return self._altura
    @property
    def area(self):
        return self._area

    @property
    def medidas(self):
        return f"Base: {self._base} \nAltura: {self.altura} \nÁrea: {self.area}"

    @base.setter
    def base(self, base = 0):
        if base >= 0:
            self._base = base

    @altura.setter
    def altura(self, altura = 0):
        if altura >= 0:
            self._altura = altura

    @area.setter
    def area(self, valores):
        if isinstance(valores, tuple) and len(valores) == 2:
            base, altura = valores
            if base >= 0 and altura >= 0:
                self._base = base
                self._altura = altura
                self._area = base * altura
            else:
                self._area = None
        else:
            raise ValueError("A área deve ser definida com uma tupla (base, altura).")



r1 = Retangulo(8,4)
inspect(r1, private=True, methods=True)

r1.base = 12
r1.altura = 33

r1.area = (9,3)
print(r1.medidas)