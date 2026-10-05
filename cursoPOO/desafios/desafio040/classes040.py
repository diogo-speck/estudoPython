# Implemente duas Classes JSON e XML para exportar dados de maneira funcional
from desafios.desafio039.classes039 import *
import random



class JSON():
    """
        Classe que exportar dados de maneira funcional em formato JSON
        Possui o método exportar(objeto())
    """
    def exportar(self, objeto):
        #return(f"Exportando dados de {objeto} para JSON")
        from json import dumps

        lista = []
        for item in objeto:
            lista.append(item.__dict__) 
        txt = dumps(lista, ensure_ascii=False, indent=2)
        return txt


class XML():
    """
        Classe que exportar dados de maneira funcional em formato XML
        Possui o método exportar(objeto())
    """
    def exportar(self, objeto):
        #return(f"Exportando dados de {objeto} para XML")
        import xml.etree.ElementTree as ET

        nome = objeto[0].__class__.__name__.lower()
        pai = ET.Element("dados")
        for item in objeto:
            filho = ET.SubElement(pai, nome)
            for chave, valor in item.__dict__.items():
                neto = ET.SubElement(filho,chave)
                neto.text = str(valor)
        ET.indent(pai, space="\t")
        txt = ET.tostring(pai, encoding="unicode", xml_declaration=True)
        return txt



class Login():
    def __init__(self, user, email, senha=""):
        if not validar_dado(User(), user):
            self.user = str(random.randint(10000, 99999999999999999999)).zfill(20)
            print(f"Seu novo usuário: {self.user}")
        else:
            self.user = user

        while not validar_dado(Email(), email):
            email = input("Digite outro e-mail: ")
        self.email = email

        senha = user+"_123"
        while not validar_dado(Senha(), senha):
            senha = input("Digite outro senha: ")
        self._senha = senha


class Estudante():
    def __init__(self, nome, serie="1ª", curso=None):
        self.nome = nome
        self.serie = serie
        self.curso = curso



def exportar_dados(tipo, objeto):
    print(tipo.exportar(objeto))