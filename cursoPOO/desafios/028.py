# Implemente uma Classe Termostato, onde vamos simular o funcionamento de um termostato simples
from rich import print, inspect
from rich.panel import Panel

class Termostato:
    """
        Classe que instancia um objeto chamado Termostato que inicia em 24 °C e pode aumentar e diminuir a temperatura,
        além disso, tem um limite mínimo de temperatura (16 °C) e um máximo (30 °C)
        ex. t1 = Termostato()
        Possui 2 métodos:
        aumentar ou diminuir com + -
        ex. t1.setTemp()
        confere se o valor dito é múltiplo de 0,5 e está no intervalo de 16 e 30
        ex. t1.getTemp()
        vai aumentando ou diminuindo 0,5 até chegar no valor informado
    """

    temp_min: int = 16
    temp_max: int = 30

    def __init__(self):
        self.__temp = 24.0

    def setTemp(self, temp=24.0):
        try:
            if round(temp * 2) % 1 == 0 and self.temp_min <= temp <= self.temp_max:
                self.__temp = temp
                return self.__temp
            else:
                print("Número fora do intervalo ou não múltiplo de 0,5")
        except:
            print("A temperatura informada não é um número")
            return 0

    def get_temp_value(self):
        return self.__temp

    def getTemp(self):
        total_range = self.temp_max - self.temp_min
        progresso = int(((self.__temp - self.temp_min) / total_range) * 20)  # 20 blocos

        if self.__temp < 20:
            cor = "blue"
        elif self.__temp < 26:
            cor = "green"
        else:
            cor = "red"

        barra = "█" * progresso + " " * (20 - progresso)
        return Panel(
            f"[blue]{self.temp_min}°C[/] [{cor}]{barra}[/] [red]{self.temp_max}°C[/]\nTemperatura atual: {self.__temp} °C",
            title="Termostato", width=50)


t1 = Termostato()

t1.setTemp(25)
inspect(t1, private=True, methods=True)
print(f"A temperatura atual é {t1.get_temp_value()}")

while True:
    print(Panel("+ - Aumenta a Temperatura \n- - Diminui a Temperatura \n16-30 - Escolhe a Temperatura", title="Menu", width=40))
    escolha = input("Escolha: ")
    if escolha == "+":
        t1.setTemp(t1.get_temp_value() + 0.5)
    elif escolha == "-":
        t1.setTemp(t1.get_temp_value() - 0.5)
    else:
        try:
            valor = float(escolha)
            t1.setTemp(valor)
        except ValueError:
            break

    print(t1.getTemp())