Comentários sobre o curso "Python Orientado a Objetos" do canal Curso em Vídeo

A "Crise de ‘Software’" surgiu em 1960
A característica que identifica as linguagens lineares são os desvios forçados com o "goto"
O Criador da linguagem "Smalltalk" foi Alan Kay
A linguagem simula foi um superconjunto da linguagem Algol60
As duas últimas letras da sigla "OOAD" significam Analysis/‘Design’
COMERN C-confiavel, O-oportuno, M-manutenivel, E-extensivo, R-reutilizavel e N-Natural
Alterações não muda outra área; Pode ser feito simultaneamente; Mais fácil de atualizar;
Sistema não estático (tudo pode crescer de forma útil); Utilizado em outros sistemas
Mais fácil de entender: (Classe = Molde) != Objeto
atributos (coisas que a classe vai ter) e métodos (coisas que eu posso fazer com a classe) ()
Instância = ação de instanciar/seguir o padrão da classe para criar o objeto
"Um objeto é uma instância de uma classe, definido por algo material/abstrato a partir de uma classe, descrito por seus atributos, métodos e estado"
Todos os atributos têm valores de um estado
Ex. Objeto biscoito, instanciar a Classe molde de coração (colocar no molde), atributo inteiro, estado verdadeiro, método comer (muda o estado)
Atividade: Objeto1(concreto)-computador, classe marca hp, atributo ligado, estado verdadeiro 
Objeto2(abstrato)-previsão do tempo, classe: dia limpo, atributo chuva, estado falso
Objetos são variáveis, compostas ou não, evoluídas, pois conseguem além de armazenar dados nomeando eles, podem executar funcionalidades
Atributos = dados; Métodos = Funcionalidades
Biblioteca rich é uma alternativa para deixar o terminal mais visual
4 Pilares da POO: Herança (superclasses e subclasses), Encapsulamento (proteger partes importantes do código), Abstração (capacidade de simplificar as coisas) e Polimorfismo (atividades de mesmo nome de maneiras diferentes)
Herança em programação é um tipo de relacionamento entre itens gerais (ancestrais) e tipos mais específicos (descendentes) desses itens, que herdam atributos e métodos (características e comportamentos) dos níveis superiores (extensibilidade)
Principais vantagens: Reútilização de código, organização hierárquica (mais fácil de ler e entender), mais fácil de fazer manutenção e dá suporte ao Polimorfismo
Generalização do tipo "é um"
Abstração é a prática de ignorar o irrelevante e focar-se estritamente no essencial
Principais vantagens: Maior legibilidade (absorve só o essencial); Padronização (generalização/abstrata); Simplificação (especializada); Segurança (não detalhamento)
Abstração de dados - Ignora algumas informações desnecessárias (ex. altura e peso de uma pessoa que vai fazer um cadastro)
Abstração de processos - Ignora como um método funciona detalhadamente (ele funciona e ponto)
Método Concreto é um método na classe abstrata que é {abstract} (não definido ainda) e nunca é instanciada só definida para as subclasses
Um conjunto de vários métodos abstratos é a interface pública de uma classe
Uma classe abstrata pode ter métodos abstratos que deverão ser implementados nas subclasses
Quando uma classe abstrata tem um método concreto (que serve para todas as subclasses), chamamos esse método de "DRY" - Don't Repeat Yourself
Por padrão o Python não tem métodos abstratos, somente importando o ABC - ‘Abstract’ Base Classes
Diferentemente do Java que usa ‘abstract’ class
Encapsulamento - Integridade do sistema, proteção do estado interno do objeto contra interferência externa (segurança, controle, manutenível e flexibilidade)
Exemplo de um Controle Remoto - Protege com uma "Capsula"
Visibilidade para atributos: Public +; Protected #; Private -; Exemplo de Java
Público - Acessível de qualquer lugar (todo o escopo)
Protegido - Disponível para a Classe principal e as subclasses
Privado - Somente na Classe principal
Em Python há uma convenção, mas ele não proíbe a mudança Exemplo de Python
Por padrão Público não tem nada antes, Protegido tem um "_" antes e Privado tem "__" antes
Acesso a dados de Encapsulamento → Getters/"Setters" (métodos acessores tipo Java) e @property (no caso do Python)
"set" determina o que pode e o que não pode e "get" recebe o valor após passar pelo "set"