'''
Python enables programs to be written compactly and readably. Programs written in Python are typically much shorter than equivalent C, C++, or Java programs, for several reasons:
    - the high-level data types allow you to express complex operations in a single statement;
    - statement grouping is done by indentation instead of beginning and ending brackets;
    - no variable or argument declarations are necessary.
'''
# Todo número resultante de uma divisão é um tipo float (floating-point number)
# ToDo floor division and get just the integer result you can use the //
# Todo intervalo segue esse padrão (começo(incluso), fim(não-incluso), o quanto que vai pular)
# Todo tipo de função cria seu próprio espaço de variáveis
# Todo tipo de função sempre retorna algo, apesar de não ter um return, ela ainda retorna algo nulo. Esse é um padrão que todo tipo de dado mutável em python segue
# Todo método em Python dentro de uma classe deve receber self como primeiro parâmetro, que representa a própria instância
# Todo tipo de classe precisa ter um método especial chamado __init__() por padrão
# Todos os métodos de python são do tipo virtual como o de C++

import random
from collections import deque
import ipaddress
import sys
import math
import json
from dataclasses import dataclass

class MyEmptyClass:
    pass # classe de uma função que não faz nada, mas se instânciada a mais de uma váriavel de uma vez só dá erro
    ...

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome

class Animal: #superclasse
    def __init__(self, especie):
        self.especie = especie

    def falar(self):
        print (f"O que {self.especie} fala?")
    
class cachorro(Animal): #subclasse
    def __init__(self):
        super().__init__("Cachorro" )# chama o init da superclasse
    
    def falar(self):
        super().falar() # chama o método da superclasse
        print ("Au au")

class gato(Animal): #subclasse
    def __init__(self):
        super().__init__("Gato")
    
    def falar(self):
        super().falar()
        print ("Miau")

@dataclass
class Employee:
    name: str
    dept: str
    salary: int

class Complex:
    def __init__(self, realpart, imgpart):
        self.r = realpart
        self.i = imgpart

    def __str__(self):
        return f"{self.r}+{self.i}i"

def soma (a,b): # função que soma 2 valores
    return a+b

def fib(n):    # função que printa a sequência de Fibonacci até n
    fibo = []
    a, b = 0, 1
    while a < n:
        fibo.append(a)
        a, b = b, a+b # Atualização simultânea, por isso não precisa salvar o valor anterior de a
    return fibo

def ask_ok(prompt, retries=4, reminder='Por favor, tente novamente!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes', 's', 'si', 'sim'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope', 'na', 'nã', 'nao', 'não'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('Resposta inválida')
        print(reminder)

def adicionar(item, lista=None):
    if lista is None: # ou seja, se ela tem algum valor dentro
        lista = []

    lista.append(item)
    return lista

def embaralhar(lista):
    copia = lista[:]
    random.shuffle(copia)
    return copia # retorna os argumentos

def remover(lista, item):
    queue = deque(lista)
    queue.remove(item)
    return list(queue) # converte de deque para o tipo lista, essa é a função

def distancia_ipv4(ip1: str, ip2: str) -> int:
    # Retorna a diferença numérica entre dois IPv4
    addr1 = int(ipaddress.IPv4Address(ip1))
    addr2 = int(ipaddress.IPv4Address(ip2))
    return abs(addr1 - addr2)

def mesma_subrede(ip1: str, ip2: str, mascara: str) -> bool:
    # Verifica se dois IPs estão na mesma sub-rede
    rede = ipaddress.IPv4Network(mascara, strict=False)
    return ipaddress.IPv4Address(ip1) in rede and ipaddress.IPv4Address(ip2) in rede

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

print("Testando a Programação Orientada ao Objeto em Python")
a = float(input("Digite o 1º valor para somar: "))
b = float(input("Digite o 2º valor para somar: "))
print(f"A soma dos valores {a} + {b} é = {soma(a,b)}")
print(f"{a/b} >= {a//b}")
c = a**b
round(c, 0)
print("Os valores elevados são", c)
c = vars
print(c)
print(r'C:\this\name')
print('C:\this\name')
print("""
    Testando
    Pulando Linhas
      """)
print(3*'bla')
print("Escrevendo "
      "separado tudo junto"
      " e tudo junto separado")
d,e = 'diogo',"teste"
print(f"{d[-2]}")
print(f"{d[0:3]}")
cores = ["azul","vermelho", "amarelo"]
chroma = cores
chroma.append("Azul Bebê Jujuba de Maçã Verde")
print(cores)
cores = chroma[:]
cores[-1] = "verde"
print(cores)
chroma[:] = []
print(chroma)
print(e, end=',\n')
vv = {"Diogo":"Admin", 'Enzo':'Admin', "Jia":'Admin', 'Caique':"Admin", "Gustavo":"Membro", "Gustavo":"Membro", "Gustavo":"Membro", "Hugo":"Membro", "Daniel":"Membro", "Eric":"Membro", "Ferret":"Membro", "João":"Membro", "Malu":"Membro", "Vinícius":"Membro", "Wesley":"Membro"}

for membros, status in vv.copy().items():
    if status == 'Membro':
        del vv[membros]

admins = {}

for membros, status in vv.items():
    if status == "Admin":
        admins[membros] = status

print(admins)
x,y = map(int, input("Insira uma coordenada do plano cartesiano (-1,1 para x=-1 e y=1): ").split(",")) # tenta converter cada caractere da string em inteiro
point = (x,y)
match point:
    case (0, 0): # tupla
        print("Origem")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y) if x == y:
        print(f"Y=X em {x}")
    case (x, y):
        print(f"X={x}, Y={y}")
        print("Não está na diagonal")
    case _: # default
        raise ValueError("Não é um ponto")

f = int(input("Digite o limite para a sequência de Fibonacci: "))
print(fib(f))
resposta = ask_ok("Você está na frente do computador? ", 2, 'Somente sim ou não!')
if resposta:
    print("Bom proveito")
elif resposta == False:
    print("Entendi, melhor virar então")
else:
    print("Não precisava responder mesmo")
ordem = []
for i in range(8):
    bit = adicionar(input("Adicione algo na lista bit, lembrando que ela só adiciona 1 valor por vez porquê simula um bit: "))
    print(bit)
    ordem.append(bit)
print("")
desordem = embaralhar(ordem)
for i in range(4):
    for j in range(2):
        indice = i * 2 + j
        print(f"{desordem[indice]}", end="")
    print("")
print("")
for i in range(2):
    for j in range(4):
        indice = i * 4 - j
        print(f"{desordem[indice]}", end="")
    print("")

continuar = True
add = ""
lista2= []
vezes = 0
while(continuar):
    add = input("Adicione algo na lista: ")
    lista2.append(add)
    confirmar = input(f"{lista2} \nDeseja adicionar algo a mais? (s/n) ")
    if confirmar == "n":
        continuar = False
while(continuar == False):
    add = input("O que deseja remover: ")
    vezes = lista2.count(add)
    if vezes> 0:
        lista2 = remover(lista2,add) # tem que atribuir o return da função na variável
    confirmar = input(f"{lista2} \nDeseja remover algo a mais? (s/n) ")
    if confirmar == "n":
        continuar = True
print(f"Sua lista final ficou assim: {lista2}")

quadrados = [x**2 for x in range(10)]
print(quadrados)
print ([(dado1,dado2) for dado1 in [1,2,3,4,5,6] for dado2 in [1,2,3,4,5,6] if x or y])

h = sorted(set(("amora")))
l = sorted(set(("girar")))
print(f"O {h} vai {l}") # "O amor vai agir", porquê o set elimina letras repetidas e coloca em ordem alfabética

carrosE = {"BYD" : "Dolphin", 'GWM': 'Haval H6', 'Chevrolet': 'Bolt EV', 'Volvo': "XC60", 'BMW': 'X3', 'Ferrari': None, 'Lamborghini': None, 'McLaren': None}
# print(carrosE) printa do jeito que está definida
print(f"Marcas de Carro: {list(carrosE)}")
print(f"Modelos de carros elétricos: {list(carrosE.values())}")
carrosE["Ferrari"] = "Luce"
print(f"O carro elétrico da Ferrari é o {carrosE["Ferrari"]}")
del carrosE["BYD"] # não funciona porquê é imutável
carrosE["BYD"] = "Fora de estoque"
print(f"{carrosE["BYD"]=}\n")

rpg = {'Alaúde,':'o bardo que não cala a boca', 'Pancrácio,':'o guerreiro diplomata da porrada', 'Amnésios,':'o conjurador esquecedor de feitiços', 'Santino,':'o paladino que mais comete pecados', 'Mestre Cuca Beludo,':'o cozinheiro guloso', 'Sr.Manezero,':'o mago esgotado'}
for nomes, sobre in sorted(rpg.items()): # sorted para organizar em ordem alfabética
    print(nomes, sobre)

print(0==0.0)
ip_a = "192.168.0.1"
ip_b = "192.168.0.100"
confere = mesma_subrede(ip_a,ip_b,"192.168.0.0/24")
if confere:
    estao = "estão"
else:
    estao = "não estão"

print(F"Os IPs {estao} na mesma rede e a distância entre {ip_a} e {ip_b}: {distancia_ipv4(ip_a, ip_b)}") # usando um módulo
print(sys.path)
print()
m = 1/3
print(f"{m:.2f}")
n = input("Digite um número de celular para conferir se é válido ou não (ex. 5547999999999): ")
if len(n) == 13:
    print(f"O número  +{n[0:2]} ({n[2:4]}){n[4:9]}-{n[9:]} é válido")
else:
    print(f"O número {n} não é válido")
print ("I'm an {} who says \"{}\"".format("Owl", "OOO"))
print()
o = 10*10 # define o número máximo
p = math.floor(math.log10(o)) + 1 # define a quantidade de digitos matematicamente
for i in range(1,11):
    for j in range(1,11):
        print(f"{(i*j):{p}d}", end=" ") # formata em p dígitos
    print()
print()

# Tabela desalinhada:
# for i in range(1,11):
#     for j in range(1,11):
#         print("{}".format(i*j), end=" ")
#     print()

print('The value of pi is approximately %5.3f.' % math.pi)

# Arquivo JSON
config = {
    "usuario": "Diogo",
    "idioma": "pt-BR",
    "tema": "escuro",
    "pontuacao": [10, 20, 30]
}

# --- Salvando em arquivo JSON ---
with open("config.json", "w", encoding="utf-8") as f: # escrevendo
    json.dump(config, f, ensure_ascii=False, indent=4)

print("Configurações salvas em config.json")

# --- Lendo de arquivo JSON ---
with open("config.json", "r", encoding="utf-8") as f:
    carregado = json.load(f)

print("Configurações carregadas:", carregado)

# testando o try para abrir um arquivo já usando file.close()
try: 
    with open("data.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File \"data.txt\" not found.") # não existe
except Exception as e:
    print(f"Unexpected error: {e}")
finally:
    print("Próximo arquivo") # aparece em qualquer caso, se for no try ou na except

try:
    with open("config.json", "r") as file: # existe
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File \"config.json\" not found.")
except Exception as e:
    print(f"Unexpected error: {e}")
finally:
    print("Eu sou inevitável") # aparece em qualquer caso, se for no try ou na except

p1 = Pessoa("Maria")
p2 = p1   # p2 aponta para o mesmo objeto que p1

print(p1.nome)  # Maria
print(p2.nome)  # Maria

novonome = input("Digite um nome: ")
p2.alterar_nome(novonome)
print(p1.nome)  # (mudou tanto o 1 quanto o 2)
print(p2.nome)
print("Essas Marias vai com as outras...")

q = Complex("2","3")
q.r, q.i
print(q) # se não converter para __str__ ela mostraria apenas o endereço do objeto ex. <__main__.Complex object at 0x00000195D6CBA660>
r,s = input("Digite um número real e imaginário (no padrão 1 2 para 1+2i): ").split(" ")
# print(r,s) só printa a tupla
comp = Complex(r,s)
print(comp)

t = Animal("Raposa")
u = cachorro()
v = gato()
u.falar()
v.falar()
t.falar()
print()

diogo = Employee("Diogo", "TI", 1621)
print(f"{diogo.name} trabalha no setor de {diogo.dept} e ganha R${diogo.salary},00")

w = input("Escreva algo: ")
for char in reverse(w):
    print(char, end='')
list(w[i] for i in range(len(w)-1, -1, -1))