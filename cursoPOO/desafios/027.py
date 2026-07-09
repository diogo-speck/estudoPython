# Diagrama de Classes de RPG: Personagem (abstrato) com atributos de nome, vida e os seus golpes sendo concretos
# Além disso, terá a habilidade curar sendo um abstractmethod e receber_dano e atacar (um alvo e a força)
# Terá pelo menos 2 classes filhas Guerreiro e Mago

from abc import ABC, abstractmethod
from rich import print, inspect
import random

class Personagem(ABC):
    def __init__(self, nome, vida=1):
        self.nome = nome
        self.vida, self.max_vida = vida, vida
        self.golpes = [] # Ataques e os seus respectivos danos

    def aprender_ataque(self, nome, dano):
        self.golpes.append(nome)
        self.golpes.append(dano)

    def receber_dano(self, dano):
        self.vida-=dano
        print(f"O(a) {type(self).__name__} {self.nome} recebeu {dano} de dano, agora sua vida é de {self.vida}")

    def atacar(self, alvo, ataque=0):
        if self.vida > 0 and alvo.vida > 0:
            golpe = self.golpes[ataque+1]
            d20 = random.randint(1,20)
            if d20 >10:
                alvo.receber_dano(golpe)
                return f"O(a) {self.nome} tirou {d20} no dado e conseguiu atacar o(a) {alvo.nome} com o golpe {self.golpes[ataque]} dando {golpe} de dano"
            else:
                return f"O(a) {self.nome} tirou {d20} no dado e NÃO conseguiu atacar o(a) {alvo.nome} com o golpe {self.golpes[ataque]}"
        else:
            if alvo.vida > 0:
                return f"O(a) {self.nome} perdeu todos os ponto de vida e NÃO conseguiu atacar o(a) {alvo.nome} com o golpe {self.golpes[ataque]}"
            else:
                return f"O(a) {alvo.nome} já tinha perdido todos os ponto de vida e por misericórdia {self.nome} NÃO atacou"

    @abstractmethod
    def curar(self, qtd):
        pass


class Guerreiro(Personagem):
    def curar(self, qtd):
        if self.vida != self.max_vida and self.vida > 0:
            d20 = random.randint(1, 20)
            if d20 > 10:
                if self.vida+qtd > self.max_vida:
                    vida = self.max_vida-self.vida
                    self.vida = self.max_vida
                    return f"O(a) {self.nome} tirou {d20} no dado e conseguiu curar {vida} de vida com suas ataduras, vida atual: {self.vida} (MAX)"
                else:
                    self.vida+=qtd
                    return f"O(a) {self.nome} tirou {d20} no dado e conseguiu curar {qtd} de vida com suas ataduras, vida atual: {self.vida}"
            else:
                return f"O(a) {self.nome} tirou {d20} no dado e NÃO conseguiu se curar, vida atual: {self.vida}"
        else:
            if self.vida < 0: vida=0
            return f"O(a) {self.nome} não consegue se curar (Vida: {self.vida}/{self.max_vida})"


class Mago(Personagem):
    def curar(self, qtd):
        if self.vida != self.max_vida and self.vida > 0:
            d20 = random.randint(1, 20)
            if d20 > 5:
                if self.vida+qtd > self.max_vida:
                    vida = self.max_vida-self.vida
                    self.vida = self.max_vida
                    return f"O(a) {self.nome} tirou {d20} no dado e conseguiu curar {vida} de vida com suas magias, vida atual: {self.vida} (MAX)"
                else:
                    self.vida+=qtd
                    return f"O(a) {self.nome} tirou {d20} no dado e conseguiu curar {qtd} de vida com suas magias, vida atual: {self.vida}"
            else:
                return f"O(a) {self.nome} tirou {d20} no dado e NÃO conseguiu se curar, vida atual: {self.vida}"
        else:
            if self.vida < 0: vida = 0
            return f"O(a) {self.nome} não consegue se curar (Vida: {self.vida}/{self.max_vida})"



print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⣿⣿⣿⣿⡿⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢠⠀⠀⢠⡏⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠓⠈⠀⢀⠎⡰⠙⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⡜⠒⡄⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣟⠏⣷⣿⣯⢏⡾⠿⠃⠀⠀⠀⢠⣶⢧⡘⢀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣀⣷⠀⠀⠙⠳⢿⣿⣿⢂⣤⠈⠠⠀⠉⠀⠀⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢀⠣⣿⡄⠀⠀⠀⠀⠉⠉⣀⠀⠀⠀⠀⠀⠀⠀⡐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠠⣿⣷⣖⠀⣀⣤⣤⡾⣿⠐⣆⠀⢀⠀⠄⠘⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠧⣌⠈⠡⠿⡟⠉⣩⢽⣯⠀⣌⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢐⣪⣆⠀⡁⠀⣴⠉⠳⠿⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡰⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣎⢧⠾⠋⠟⠓⠐⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⠶⠈⢀⡆⠇⠀⠀⠀⣀⣶⣾⣿⣿⠀⢹⣿⡈⣀⠶⠀⠈⠈⠀⠀⠀⡀⠀⠀⠀⠀⡇⢶⠶⢆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠄⢨⡤⠤⠒⠁⠀⠃⢀⠂⠡⠌⣾⣿⣿⡟⠸⡄⠈⠉⠍⢀⣠⡄⠀⠀⡀⠀⠀⠀⠀⠀⡐⢈⠰⡌⢢⢉⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣬⠀⠩⠆⠀⠊⠀⠀⡁⠠⡈⠔⠰⢚⣿⣿⣿⣷⣫⠐⡀⠀⠙⠛⠃⠀⠀⠂⠁⠀⠀⠀⠐⣀⠂⠠⠈⠁⠎⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢧⠀⡀⠀⠀⠀⠀⠀⡧⠐⠠⠈⡔⠩⢯⣿⣿⣿⣷⣯⡐⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠁⢀⠒⠀⢂⠁⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢣⠀⠀⠀⠀⠀⠀⠀⡄⠀⢂⠡⡀⠩⠿⣿⢿⣻⣷⡻⣷⣻⠆⡀⠀⠀⠀⠀⠀⠀⢀⠂⠀⠂⢀⠡⠈⡘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡐
⠸⠀⡆⠀⠀⠄⠀⢸⡇⠀⠂⠀⠐⠠⢙⣻⠿⡿⣿⣝⠿⣏⣷⣘⡀⠀⠀⠀⠀⠀⡂⠄⠁⢀⠂⡀⠡⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠦⣱
⠀⠇⡇⠀⠀⠀⠀⢰⠃⠀⠀⠀⠀⠀⡄⢢⣹⣭⢷⣛⣳⣶⡣⠌⡑⠆⠀⠀⣰⠠⠀⠀⠐⡀⢈⠀⠁⠂⠀⠀⠀⠀⠀⠀⠀⠀⢀⣜⢴⢳
⠀⡏⠇⢀⠩⢀⠀⠘⠀⠀⠄⠠⢀⡔⡸⣻⢿⣿⣿⣷⣿⣿⣷⡙⣧⣤⣶⣴⣿⡃⣀⠄⠀⠠⠀⠈⠄⠂⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿
⠀⠄⠸⠘⣠⣄⡀⡆⢀⠣⡈⢥⣚⣽⣿⣿⣿⣾⣿⣿⣿⣿⣷⡃⠌⣿⠿⣿⣿⢛⣷⣮⡐⠠⢁⡈⠀⠀⠀⠀⠀⠀⠀⠀⠠⣿⣿⣻⡿⣝
⠀⠄⠀⡄⠟⠞⢠⠀⢈⠆⡑⢢⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢸⡀⣽⣿⣿⣿⣿⣧⡖⢄⡦⠁⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣷⡿⡁
⠀⢀⠀⠃⣠⢀⠀⠀⡀⠼⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⠇⠀
⠀⠈⢀⠀⠀⠠⠀⢔⡁⠒⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⣿⣾⣽⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⢫⠄⠀
⠀⠀⢃⡀⠌⠀⠰⣬⣭⡤⡻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣭⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⡒⠁⠴⠀⠰⠀⠀⢠⣿⣿⣿⢏⡃⠀⠀
⠀⠀⠆⠁⠀⢤⢳⣷⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⢤⣿⣿⣿⣿⣿⣿⣿⢏⣴⡄⢥⡶⢄⡀⡄⠐⡜⢸⣿⣿⣏⠎⠄⠀⠀
⠀⠀⠈⢤⡟⣶⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢣⢿⣿⣿⣿⣿⣿⠷⣃⠲⡛⠏⠁⠢⠀⠈⠀⠂⣿⣿⣿⡌⢢⠐⠀⠀
""")


p1 = Guerreiro("Kratos", 2000)
p2 = Mago("Merlin", 3000)

p1.aprender_ataque("Soco", 1000)
p1.aprender_ataque("Pulo Giratório", 1500)
p1.aprender_ataque("Golpe de Machado", 3000)

p2.aprender_ataque("Bola de Fogo", 1500)
p2.aprender_ataque("Raio de Luz", 2000)
p2.aprender_ataque("Magia Estática", 0)

print(p1.atacar(p2, 4))
print(p1.atacar(p2, 4))
print(p2.curar(5000))

print(p2.atacar(p1), 2)
#inspect(p1)
#inspect(p2)


print("""[white]
                                  ....
                                .'' .'''
.                             .'   :
\\                          .:    :
 \\                        _:    :       ..----.._
  \\                    .:::.....:::.. .'         ''.
   \\                 .'  #-. .-######'     #        '.
    \\                 '.##'/ ' ################       :
     \\                  #####################         :
      \\               ..##.-.#### .''''###'.._        :
       \\             :--:########:            '.    .' :
        \\..__...--.. :--:#######.'   '.         '.     :
        :     :  : : '':'-:'':'::        .         '.  .'
        '---'''..: :    ':    '..'''.      '.        :'
           \\  :: : :     '      ''''''.     '.      .:
            \\ ::  : :     '            '.      '      :
             \\::   : :           ....' ..:       '     '.
              \\::  : :    .....####\\ .~~.:.             :
               \\':.:.:.:'#########.===. ~ |.'-.   . '''.. :
                \\    .'  ########## \ \ _.' '. '-.       '''.
                :\\  :     ########   \ \      '.  '-.        :
               :  \\'    '   #### :    \ \      :.    '-.      :
              :  .'\\   :'  :     :     \ \       :      '-.    :
             : .'  .\\  '  :      :     :\ \       :        '.   :
             ::   :  \\'  :.      :     : \ \      :          '. :
             ::. :    \\  : :      :    ;  \ \     :           '.:
              : ':    '\\ :  :     :     :  \:\     :        ..'
                 :    ' \\ :        :     ;  \|      :   .'''
                 '.   '  \\:                         :.''
                  .:..... \\:       :            ..''
                 '._____|'.\\......'''''''.:..'''
                            \\
""")