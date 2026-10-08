import os
import ipaddress


def lerArquivo(nome):

    final = nome + "Organizados"

    nome = "multifunctional-utilities/procurarArquivos/" + nome

    if not os.path.isfile(nome):
        print(f"Arquivo não encontrado: {nome}")
        return

    extensao = nome.split(".")[-1].lower()

    nome_saida = os.path.splitext(nome)[0] + "Organizados" + ".txt"

    # --- Lendo o arquivo ---

    with open(nome, "r", encoding="utf-8") as f:
        carregado = f.read()

    print(f"Arquivo lido")

    linhas = carregado.splitlines()

    resultado = """
ACME Inc.                      Uso do espaço em disco pelos usuários

------------------------------------------------------------------------------------

Nr. Usuário                    Espaço Utilizado          % do uso
"""

    total = 0
    qtd = 0

    # --- Calculando o total ---

    for linha in linhas:

        if not linha.strip():
            continue

        espaco_usuario = float(linha.split()[-1])

        total += espaco_usuario / 1000000
        qtd += 1

    # --- Separar nomes e espaço ---

    for numero, linha in enumerate(linhas, start=1):

        if not linha.strip():
            continue

        nome_usuario = linha.split()[0]
        espaco_usuario = float(linha.split()[-1]) / 1000000

        porcentagem = (espaco_usuario / total) * 100

        resultado += (
            f"{numero:<5}"
            f"{nome_usuario:<25}"
            f"{espaco_usuario:>10.2f} MB"
            f"{porcentagem:>20.2f}%\n"
        )

    resultado += f"\nEspaço total ocupado: {total:.2f} MB\n"
    resultado += f"Espaço médio ocupado: {total/qtd:.2f} MB"

    # --- Salvando em arquivo txt ---

    with open(nome_saida, "w", encoding="utf-8") as f:
        f.write(resultado)

    print(f"Usuários organizados salvos {nome_saida}")


print(f"Procurando em {os.getcwd()}")

arquivo = input(
    "\nDigite o nome do arquivo com os usuários em txt (ex: user.txt): "
)

lerArquivo(arquivo)

#Implementar Futuramente odenação, n primeiros que o usuário escolher, mostrar o arquivo em um html