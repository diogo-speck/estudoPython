# Comentários sobre o curso "Python Orientado a Objetos" do canal Curso em Vídeo
# A "Crise de Software" surgiu em 1960
# A característica que identifica as linguagens lineares são os desvios forçados com o "goto"
# O Criador da linguagem "Smalltalk" foi Alan Kay
# A linguagem simula foi um super conjunto da linguagem Algol60
#  As duas últimas letras da sigla "OOAD" significam Analysis/Design
# COMERN C-confiavel, O-oportuno, M-manutenivel, E-extensivo, R-reutilizavel e N-Natural
# Alterações não muda outra área; Pode ser feito simultaneamente; Mais fácil de atualizar;
# Sistema não estático (tudo pode crescer de forma útil); Utilizado em outros sistemas
# Mais fácil de entender
# (Classe = Molde) != Objeto
# Nome, +-# atributos (coisas que a classe vai ter) e métodos +-# (coisas que eu posso fazer com a classe) ()
# Instância = ação de instanciar/seguir o padrão da classe para criar o objeto
# "Um objeto é uma instância de uma classe, definido por algo material/abstrato a partir de uma classe, descrito por seus atributos, métodos e estado"
# Todo atributo tem valores de um estado
# Ex. Objeto biscoito, instanciar a Classe molde de coração (colocar no molde), atributo inteiro, estado verdadeiro, método comer (muda o estado)
# Atividade: Objeto1(concreto)-computador, classe marca hp, atributo ligado, estado verdadeiro / Objeto2(abstrato)-previsão do tempo, classe dia limpo, atributo chuva, estado falso
# 

import random
from collections import deque
import ipaddress
import sys
import math

class MyEmptyClass:
    pass # classe de uma função que não faz nada, mas se instânciada a mais de uma váriavel de uma vez só dá erro
    ...

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


print("Testando a Programação Orientada ao Objeto em Python")
a = float(input("Digite o 1º valor para somar: "))
b = float(input("Digite o 2º valor para somar: "))
print(f"A soma dos valores {a} + {b} é = {soma(a,b)}")
print(f"{a/b} >= {a//b}")
c = a**b
round(c, 0)
print("Os valores elevados são", c)
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

h = set("amora")
l = set("girar")
print(f"O {h} vai {l}") # tem chance de ser "O amor vai agir", porquê o set elimina letras repetidas e coloca em uma ordem

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


# Depois ler https://docs.python.org/release/3.14.5/tutorial/appetite.html
# Python enables programs to be written compactly and readably. Programs written in Python are typically much shorter than equivalent C, C++, or Java programs, for several reasons:
# - the high-level data types allow you to express complex operations in a single statement;
# - statement grouping is done by indentation instead of beginning and ending brackets;
# - no variable or argument declarations are necessary.
#
# division always returns a floating-point number
# To do floor division and get just the integer result you can use the //
# entre operações de diferentes tipos de variáveis, predomina aquela que engloba a outra nos conjuntos ex. float(int)
# Strings usam "" ou '' para concatenar caracteres especiais usa-se \(alt 92) "\"" \n pula linha
# Strings armazenam os caracteres especiais também quando não são printadas
# print r serve para não realizar as ações usando \ (raw string)
# print(""" """) serve para fazer um print formatado com multiplas linhas
# não é possível concatenar uma variável e uma String literal sem + ex. prefix = 'Py' ; prefix 'thon'
# String em python é um array que pode ter seus caracteres citados usando o seu índice inclusive negativamente voltando ex. variavel[n]
# Note that since -0 is the same as 0, negative indices start from -1
# In addition to indexing, slicing is also supported. While indexing is used to obtain individual characters, slicing allows you to obtain a substring variavel[n:i]
# Python strings cannot be changed — they are immutable
# Strings are examples of sequence types, and support the common operations supported by such types
# Lists also support operations like concatenation
# Listas são mutáveis e por isso podem sofrer alterações manualmente pelo seu index ou pelo método list.append()
# Uma variável nunca copia o dado, ela só o referencia, no caso de uma lista ela vai referenciar aos mesmos itens
# É possível usar a função len() tanto em Strings quanto em listas
# In Python, like in C, any non-zero integer value is true; zero is false. 
# The condition may also be a string or list value, in fact any sequence; 
# anything with a non-zero length is true, empty sequences are false
# Quando há uma declaração composta ou um bloco melhor dizendo, é necessário sempre pular uma linha deixando ela em branco para o compilador entender que aquela sequência terminou
# Code that modifies a collection while iterating over that same collection can be tricky to get right. Instead, it is usually more straight-forward to loop over a copy of the collection or to create a new collection
# Para iterar sequências de números, uma boa opção é usar a função range(), ela gera uma progressão aritimética
# It is possible to let the range start at another number, or to specify a different increment (even negative; sometimes this is called the ‘step’)
# Segue esse padrão (começo(incluso), fim(não-incluso), o quanto que vai pular)
# Uma curiosidade de python é que para salvar desempenho, ele usa itens sucessívos nas sequências invés de criar uma lista
# We say such an object is iterable, that is, suitable as a target for functions and constructs that expect something from which they can obtain successive items until the supply is exhausted
# The break statement breaks out of the innermost enclosing for or while loop
# If a loop finishes without executing the break, the else clause executes
# Quando usado dessa forma, o else faz mais papel de try exception do que um else por si só
# Pass não faz nada, só preenche um espaço vazio
# Similar ao switch de java
# You can use the class name followed by an argument list resembling a constructor, but with the ability to capture attributes into variables
# Invés de importar a biblioteca dataclass, quando definindo funções pode apenas definir __match_args__ para dizer para o Python que a ordem a ser seguida é a mesma que definida ex. __match_args__ = ("x", "y")
# Uma variável var é vazia
# Like unpacking assignments, tuple and list patterns have exactly the same meaning and actually match arbitrary sequences. An important exception is that they don’t match iterators or strings
# The keyword def introduces a function definition. It must be followed by the function name and the parenthesized list of formal parameters
# desempacotamento de tupla = Python primeiro calcula o lado direito inteiro
# Cada função cria seu próprio espaço de variáveis
# Python adiciona a um dicionário interno as funções criadas dessa maneira: nome da variável -> valor, essa tabela existe só durante a execução da função (temporariamente/local)
# Mesmo que já exista uma variável "global", ou seja já foi definida no código, mesmo assim é possível criar uma variável com o mesmo nome que não será alterada
# Primeiro, a função procura dentro dela mesma, depois ela procura no "Enclosing", ou seja dentro de uma nested function(Funções dentro de funções), depois global (definida ao longo do código) e por fim nas Built-ins, que são funções já pré-definidas pelo Python, como len() por exemplo
# Uma função não consegue alterar o valor de uma variável global a não ser que use global váriavel
# Para alterar no enclosing usa-se nonlocal
# Essa diferença de variáveis ocorre, porquê quando refêrenciadas, as funções criam objetos diferentes, que se diferenciam das variáveis
# Uma função sempre retorna algo, apesar de não ter um return, ela ainda pode retornar algo nulo
# A method is a function that ‘belongs’ to an object and is named obj.methodname, where obj is some object (this may be an expression), and methodname is the name of a method that is defined by the object’s type
# Um exemplo de método é o append() de listas
# The in keyword tests whether or not a sequence contains a certain value
# Os valores padrão dos parâmetros são calculados no momento em que a função é criada, e não quando ela é chamada, dessa maneira a função reutiliza as variáveis
# As default, functions share subsequent calls
# In a function call, keyword arguments must follow positional arguments. All the keyword arguments passed must match one of the arguments accepted by the function
# where / and * are optional. If used, these symbols indicate the kind of parameter by how the arguments may be passed to the function: positional-only, positional-or-keyword, and keyword-only (named parameters)
# Por padrão se não existir / ou * a função aceita tanto por posição, quanto por variável
# Use positional-only if you want the name of the parameters to not be available to the user
# Use keyword-only when names have meaning and the function definition is more understandable by being explicit with names or you want to prevent users relying on the position of the argument being passed
# For an API, use positional-only to prevent breaking API changes if the parameter’s name is modified in the future
# O * “espalha” os elementos da lista como argumentos separados, desempacotando-os
# Like nested function definitions, lambda functions can reference variables from the containing scope
# Primeira linha da docstring = resumo (deve começar com letra maiúscula, deve terminar com ponto final e não precisa mencionar função, classe etc. exceto se for um verbo)
# Se houver mais linhas na docstring a segunda linha deve ficar em branco
# Depois vem o resto, descrição em múltiplas linhas e etc
# UpperCamelCase for classes and lowercase_with_underscores for functions and methods. Always use self as the name for the first method argument
# You might have noticed that methods like insert, remove or sort that only modify the list have no return value printed – they return the default None. This is a design principle for all mutable data structures in Python
# Not all data can be sorted or compared. For instance, [None, 'hello', 10] doesn’t sort because integers can’t be compared to strings and None can’t be compared to other types.
# Also, there are some types that don’t have a defined ordering relation. For example, 3+4j < 5+7j isn’t a valid comparison
# Para adicionar algo em uma lista usa-se o método .append e para retirar usa-se .pop
# Entretanto, para listas maiores que precisam de mais otimização é possível usar a coleção collections.deque para fazer a adição e a remoção de itens
# a função del das listas também pode apagar o valor armazenado de uma variável para reutilizá-la novamente
# tuplas são imutáveis
# Note that multiple assignment is really just a combination of tuple packing and sequence unpacking.
# Dicionários podem ser criados de 3 formas: lista de chaves (métodos), compreensão e por meio de construção:
# Use a comma-separated list of key: value pairs within braces: {'jack': 4098, 'sjoerd': 4127}, dict comprehension: {}, {x: x ** 2 for x in range(10)} & type constructor: dict(), dict([('foo', 100), ('bar', 200)])
# To loop over two or more sequences at the same time, the entries can be paired with the zip() function
# Para reverter um for, basta usar a função reversed antes do range
# usar sorted(set()) em uma lista, é a maneira mais idiomática de organizar uma lista eliminando repetições e colocando em ordem alfabética
# O ideal sempre que quiser alterar coisas em uma lista em um loop, é usar uma cópia da original
# módulos são a base para escrever código limpo, reutilizável e escalável em Python, você cria arquivos e cita eles em outros
# When you don’t need fancy output but just want a quick display of some variables for debugging purposes, you can convert any value to a string with the repr() or str() functions
# For objects which don’t have a particular representation for human consumption, str() will return the same value as repr(). Many values, such as numbers or structures like lists and dictionaries, have the same representation using either function
# The repr() of a string adds string quotes and backslashes
# You can use placeholders like $x and replace them with values from a dictionary
# Também pode usar números para substituir a ordem da posição referenciada na método str.format()
# len() só serve para sequências (strings, listas, tuplas, etc.)
# O método str.zfill() adiciona zeros a esquerda de uma string numérica
# Strings são fáceis de salvar e ler em arquivos, mas números e estruturas complexas (listas aninhadas, dicionários) exigem mais trabalho. Por isso, o módulo json do Python simplifica isso
# O módulo lida bem com listas e dicionários, mas serializar instâncias de classes exige esforço extra