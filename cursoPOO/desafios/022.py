# Crie uma Classe ControleRemoto, onde vamos simular o funcionamento de um controle simples (canal, volume e liga/desliga)
from rich import print
from rich.panel import Panel

class ControleRemoto:
    """
        Classe que instancia um objeto chamado ControleRemoto e atribui a ele o estado ligado = false, canal e volume = 0
        ex. c1 = ControleRemoto()
        Possui 3 métodos: 
        power() para ligar ou desligar o controle com o botão "@"
        ex. c1.power("@")
        mudarVolume() aumentar "+1" ou diminuir "-1" o volume
        ex. mudarVolume(c1.volume+1)
        mudarCanal() mudar o canal para "cima/avança" ">" ou para "baixo/volta" "<"
        ex. mudarCanal(c1.canal+1)
    """

    canal_min:int = 1
    canal_max:int = 10
    volume_min:int = 0
    volume_max:int = 10

    def __init__(self):
        self.ligado = False
        self.canal = 1
        self.volume = 0
    
    def power(self, botao):
        if botao == "@":
            if self.ligado:
                self.ligado = False
                return "Desligando..."
            else:
                self.ligado = True
                return "Ligando..."
        else:
            return "Botão errado, pressione o botão power (@)"
    
    def mudarVolume(self, volume):
        if self.ligado:
            if volume >= ControleRemoto.volume_min:
                if volume > 10:
                    volume = 10
                    return f"Volume máximo já alcançado"
                self.volume = volume
            else:
                self.volume = 0
                return f"Volume minimo já alcançado"
            return f"O volume agora está em {self.volume}"
        else:
            return "Primeiro use o controle para ligar"
        
    def mudarCanal(self, canal):
        if self.ligado:
            self.canal = ((self.canal - 1 + canal) % 10) + 1 # intervalo de 1 a 10
            return f"O canal agora está em {self.canal}"
        else:
            return "Primeiro use o controle para ligar"

c1 = ControleRemoto()
while True:
    print(Panel("@ - Botão Power \n-+ - Volume \n<> - Canal", title="Menu", width=19))
    escolha = input("Escolha: ")
    match(escolha):
        case "@":
            print(c1.power("@"))
        case "+":
            print(c1.mudarVolume(c1.volume+1))
        case "-":
            print(c1.mudarVolume(c1.volume-1))
        case "<":
            print(c1.mudarCanal(-1))
        case ">":
            print(c1.mudarCanal(1))
        case _:
            break