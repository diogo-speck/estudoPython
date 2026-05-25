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

def sum (a,b):
    return a+b

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
print(e, end=',')

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
# 4. More Control Flow Tools