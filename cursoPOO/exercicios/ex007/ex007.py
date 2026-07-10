# Exercício Avaliação
class Avaliacao:
    """
        Cria um sistema que permite fazer a avaliação de um aluno em uma matéria com uma nota de 0 a 10
    """
    def __init__(self, nome, disciplina, nota=0):
        self.nome = nome
        self._disciplina = disciplina # Protegido (#)
        self.__nota = nota # Privado (-)
        print(f"Aluno(a) {self.nome} foi matriculado(a) na disciplina de {self._disciplina}.")
    
    def __str__(self):
        return f"O(a) aluno(a) {self.nome} faz a disciplina de {self._disciplina} e está com a nota {self.__nota}."

    # Métodos Acessores
    def get_nota(self):
        return self.__nota

    def set_nota(self, nota):
        if 0 <= nota <= 10:
            self.__nota = nota
        else:
            print("Não foi possível trocar a nota (fora do intervalo).")