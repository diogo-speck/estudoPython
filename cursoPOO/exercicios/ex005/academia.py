from rich import print, inspect
from classesEx005 import * # importando as classes do módulo classesEx005

def main():
    a1 = Aluno("José", 17, "Peito", "Segunda")
    a1.estaNaAcademia()
    a1.fazerAniversario()
    print(a1.fazerMatricula())
    print(a1.fazerMatricula())
    print(a1.malhar("Costas", "Terça"))
    # inspect(a1, methods=True) equivalente a (a1.__dict__)

    p1 = Professor("Samuel", 37, "funcional", "mestre")
    p1.estaNaAcademia()
    p1.fazerAniversario()
    print(p1.darAula())
    # inspect(p1, methods=True)

    f1 = Funcionario("Claúdia", 27, "auxiliar de limpeza", "serviços gerais")
    f1.estaNaAcademia()
    print(f1)
    f1.fazerAniversario()
    print(f1.baterPonto())
    print(f1.baterPonto())
    print(f1)
    # inspect(f1.estaNaAcademia())

    # x = Pessoa("Gustavo", 48) (não posso instanciar uma classe abstrata)



if __name__ == "__main__": # boa prática para arquivos maiores e se quiser mudar o nome
    main()