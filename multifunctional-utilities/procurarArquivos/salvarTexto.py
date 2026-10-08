import os
import json
import xml.etree.ElementTree as ET
import csv
import openpyxl

def lerArquivo(nome):
    final = nome
    nome = "multifunctional-utilities/procurarArquivos/"+nome
    if not os.path.isfile(nome):
        print(f"Arquivo não encontrado: {nome}")
        return
    extensao = nome.split(".")[-1].lower()
    nome_saida = os.path.splitext(nome)[0] + ".txt"
    # --- Lendo o arquivo ---
    match extensao:
        case "txt":
            with open(nome, "r", encoding="utf-8") as f:
                carregado = f.read()
        case "json":
            with open(nome, "r", encoding="utf-8") as f:
                dados = json.load(f)
                carregado = json.dumps(dados, indent=4, ensure_ascii=False)
        case "xml":
            arvore = ET.parse(nome)
            carregado = ET.tostring(arvore.getroot(), encoding="unicode")
        case "csv":
            with open(nome, "r", encoding="utf-8") as f:
                carregado = "\n".join(", ".join(linha) for linha in csv.reader(f))
        case "xlsx":
            workbook = openpyxl.load_workbook(nome)
            carregado = ""
            for planilha in workbook:
                carregado += f"\n--- {planilha.title} ---\n"
                for linha in planilha.iter_rows():
                    carregado += ", ".join(str(celula.value) for celula in linha)
                    carregado += "\n"
        case _:
            print("Formato não suportado")
            return
    
    print(f"Arquivo {final} lido")


    # --- Salvando em arquivo txt ---
    with open(nome_saida, "w", encoding="utf-8") as f: # escrevendo
        f.write(carregado)

    print(f"Configurações salvas em {final}")



print(f"Procurando em {os.getcwd()}")
arquivo = input("\nDigite o nome do arquivo com a extensão para ser salvo em txt (ex: texto.txt): ")
lerArquivo(arquivo)