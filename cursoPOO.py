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

# Depois ler https://docs.python.org/release/3.14.5/tutorial/appetite.html