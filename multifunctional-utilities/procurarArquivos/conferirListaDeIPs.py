import os
import ipaddress

def lerArquivo(nome):
    nome = "multifunctional-utilities/procurarArquivos/"+nome
    if not os.path.isfile(nome):
        print(f"Arquivo não encontrado: {nome}")
        return
    extensao = nome.split(".")[-1].lower()
    nome_saida = os.path.splitext(nome)[0]+ "Validados" + ".txt"
    # --- Lendo o arquivo ---
    with open(nome, "r", encoding="utf-8") as f:
        carregado = f.read()
    
    print(f"Arquivo lido")

    ips = carregado.splitlines()

    # --- Conferir a válidade dos ips ---
    validos = ""
    invalidos = ""

    for ip in ips:
        try:
            ipaddress.ip_address(ip)
            validos += f"{ip}\n"
        except ValueError:
            invalidos += f"{ip}\n"

    resultado = "[Endereços Válidos]:\n"+validos+"\n[Endereços Inválidos]:\n"+invalidos

    # --- Salvando em arquivo txt ---
    with open(nome_saida, "w", encoding="utf-8") as f: # escrevendo
        f.write(resultado)

    print(f"Ips salvos em {nome_saida}")



print(f"Procurando em {os.getcwd()}")
arquivo = input("\nDigite o nome do arquivo com os endereços em txt (ex: ips.txt): ")
lerArquivo(arquivo)