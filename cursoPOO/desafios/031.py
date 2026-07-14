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
    def __init__(self, base=0, altura=0, area=0):
        self._base = None
        self._altura = None
        self._area = None

        self.base = base
        self.altura = altura

    @property
    def base(self):
        return self._base
    @property
    def altura(self):
        return self._altura
    @property
    def area(self):
        self._area = self._base * self._altura
        return self._area
    @property
    def medidas(self):
        return f"Base: {self.base} \nAltura: {self.altura} \nÁrea: {self.area}"

    @base.setter
    def base(self, base = 0):
        if not isinstance(base, float) and not isinstance(base, int):
            raise TypeError("O valor da base deve ser um número")
        if base < 0:
            raise ValueError("Valor inválido para a base")
        else:
            self._base = base

    @altura.setter
    def altura(self, altura = 0):
        if not isinstance(altura, float) and not isinstance(altura, int):
            raise TypeError("O valor da altura deve ser um número")
        if altura < 0:
            raise ValueError("Valor inválido para a altura")
        else:
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

    @medidas.setter # Pega os 2 primeiros itens da lista
    def medidas(self, valores):
        if isinstance(valores, list) and 2 <= len(valores) <= 3:
            base = valores[0]
            altura = valores[1]
            if base >= 0 and altura >= 0:
                self._base = base
                self._altura = altura
                self._area = base * altura
                try:
                    if valores[2] != self._area:
                        print(f"Área informada errada! ({self._base}*{self._altura} = {self._area} != {valores[2]})")
                except IndexError:
                    print(f"Não foi informada a área, mas ela equivale a {self._area}")
            else:
                self._area = None
        else:
            raise ValueError("As medidas devem ser definidas com uma lista (ex. [2,4] ou [2,4,8]).")


try:
    r2 = Retangulo(5,4) # Ainda possível colocar valores negativos e outras coisas
    print(r2.medidas)
    #inspect(r2, private=True, methods=True)
    try:
        r2.area = (8,10)
        #inspect(r2, private=True, methods=True)
    except ValueError as e:
        print(f"Ocorreu um erro tipo {type(e).__name__}: {e}")
    r2.medidas = [4,9,35]
    #inspect(r2, private=True, methods=True)

except ValueError as e:
    print(f"Ocorreu um erro tipo {type(e).__name__}: {e}")