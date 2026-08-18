# Implemente uma Classe Arquivo, simulando a abertura de diferentes tipos de arquivos
from rich import print, inspect
from abc import ABC, abstractmethod
from random import random

class Arquivo(ABC):
    """
        Classe abstrata que instancia um objeto chamado Arquivo onde recebe um nome, a _extensao e o tamanho (em bytes)
        Possui os atributos nome (público), #_extensao (protegido), tamanho (público) e @nome_completo (público)
        ex. a1 = Arquivo("nome", "extensao", tamanho)
        Possui 1 abstractmethod:
        abrir()
        ex. a1.abrir()
    """

    def __init__(self, nome, extensao, tamanho):
        self.nome = nome
        self.__extensao = extensao
        self.tamanho = tamanho
    
    @property
    def nome_completo(self):
        return f"'{self.nome}.{self.__extensao}'({self.tamanho/1000000}MB)"
    
    @abstractmethod
    def abrir(self):
        pass


class PDF(Arquivo):
    def __init__(self, nome:str="novo_arquivo", tamanho:int=1000):
        super().__init__(nome, "pdf", tamanho)

    def abrir(self):
        print(f"Abrindo o arquivo {self.nome_completo} no Adobe Reader")


class DOCX(Arquivo):
    def __init__(self, nome:str="novo_arquivo", tamanho:int=10000):
        super().__init__(nome, "docx", tamanho)

    def abrir(self):
        print(f"Abrindo o arquivo {self.nome_completo} no Microsoft Word")


class PNG(Arquivo):
    def __init__(self, nome:str="novo_arquivo", tamanho:int=100):
        super().__init__(nome, "png", tamanho)

    def abrir(self):
        print(f"Você abriu o arquivo {self.nome_completo} Selecione o programa de visualização de png (Adobe Photoshop, GIMP ou Paint)")


class JPEG(Arquivo):
    def __init__(self, nome:str="novo_arquivo", tamanho:int=1000):
        super().__init__(nome, "jpeg", tamanho)

    def abrir(self):
        print(f"Você abriu o arquivo {self.nome_completo} Selecione o programa de visualização de imagens jpeg (Windows Fotos ou IrfanView)")


class GIF(Arquivo):
    def __init__(self, nome:str="novo_arquivo", tamanho:int=15000):
        super().__init__(nome, "gif", tamanho)

    def abrir(self):
        print(f"Você abriu o arquivo {self.nome_completo} Selecione o programa de visualização de gifs (FastStone Image Viewer ou ScreenToGif)")