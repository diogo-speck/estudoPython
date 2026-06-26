from rich import print, inspect
from classesEx004 import Aluno, Professor, Funcionario # importando as classes do módulo classesEx004

def main():
    a1 = Aluno("José", 17, "informática", "T01")
    a1.fazerAniversario()
    print(a1.fazerMatricula())
    print(a1.fazerMatricula())
    # inspect(a1, methods=True) equivalente a (a1.__dict__)

    p1 = Professor("Samuel", 37, "biologia", "mestre")
    p1.fazerAniversario()
    print(p1.darAula())
    # inspect(p1, methods=True)

    f1 = Funcionario("Claúdia", 27, "secretária escolar", "secretaria")
    print(f1)
    f1.fazerAniversario()
    print(f1.baterPonto())
    print(f1.baterPonto())
    print(f1)
    # inspect(f1, methods=True)

if __name__ == "__main__": # boa prática para arquivos maiores e se quiser mudar o nome
    main()