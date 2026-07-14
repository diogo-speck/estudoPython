# Implemente uma Classe Termostato, onde vamos simular o funcionamento de um termostato simples
from rich import print, inspect
from rich.panel import Panel

class Termostato:
    """
        Classe que instancia um objeto chamado Termostato que inicia em 24 °C e pode aumentar e diminuir a temperatura,
        além disso, tem um limite mínimo de temperatura (16 °C) e um máximo (30 °C)
        ex. t1 = Termostato()
        Possui 1 method chamado ftemperatura para mostrar um painel com informações sobre a temperatura
        ex. t1.ftemperatura()c
        Além de um atributo validado @temperatura que confere se o valor dito é múltiplo de 0,5 e está no intervalo de
        16 e 30, se não limita ao mínimo e ao máximo
        ex. t1.temperatura = valor
    """

    temp_min: int = 16
    temp_max: int = 30

    def __init__(self):
        self.__temp = 24.0

    @property
    def temperatura(self):
        return self.__temp

    @temperatura.setter
    def temperatura(self, temp=24.0):
        if (temp * 2) % 1 == 0 and self.temp_min <= temp <= self.temp_max:
            self.__temp = temp
        elif temp > self.temp_max:
            self.__temp = self.temp_max
        elif temp < self.temp_min:
            self.__temp = self.temp_min
        else:
            print("Número não múltiplo de 0,5, temperatura mantida")


    def ftemperatura(self):
        total_range = self.temp_max - self.temp_min
        progresso = int(((self.__temp - self.temp_min) / total_range) * 20)  # 20 blocos

        if self.__temp < 20:
            cor = "blue"
        elif self.__temp < 26:
            cor = "green"
        else:
            cor = "red"

        barra = "█" * progresso + " " * (20 - progresso)
        print(Panel(
            f"[blue]{self.temp_min}°C[/] [{cor}]{barra}[/] [red]{self.temp_max}°C[/]\nTemperatura atual: {self.__temp} °C",
            title="Termostato", width=50))


t1 = Termostato()

t1.temperatura = 25.3 # Não muda porque não é múltiplo de 0,5
inspect(t1, private=True, methods=True)
print(f"A temperatura atual é: ")
t1.ftemperatura()

while True:
    print(Panel("+ - Aumenta a Temperatura \n- - Diminui a Temperatura \n16-30 - Escolhe a Temperatura", title="Menu", width=40))
    escolha = input("Escolha: ") # vai aumentando ou diminuindo 0,5 usando '+', ou '-'
    if escolha == "+":
        t1.temperatura += 0.5
    elif escolha == "-":
        t1.temperatura -= 0.5
    else:
        try:
            valor = float(escolha)
            t1.temperatura = valor
        except ValueError:
            break

    t1.ftemperatura()