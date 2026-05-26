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

class MyEmptyClass:
    pass
    ...

def sum (a,b): # função que soma 2 valores
    return a+b

def fib(n):    # função que printa a sequência de Fibonacci até n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b # Atualização simultânea, por isso não precisa salvar o valor anterior de a
    print()


print("Testando a Programação Orientada ao Objeto em Python")
a = float(input("Digite o 1º valor para somar: "))
b = float(input("Digite o 2º valor para somar: "))
print(f"A soma dos valores {a} + {b} é = {sum(a,b)}")
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
fib(f)


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
# 4.9. More on Defining Functions