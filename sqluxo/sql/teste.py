import sqlite3
from pathlib import Path
from api import *

# Autenticar no Kaggle
conectar_kaggle()

# Caminho da pasta onde ficará o banco
pasta = Path(
    "/home/diogospeck/Documents/Prog/estudoPython/sqluxo/sql/dataset"
)

pasta.mkdir(parents=True, exist_ok=True)

# Caminho do banco SQLite
banco = pasta / "banco.db"

# Conectar ao banco
conexao = sqlite3.connect(banco)
cursor = conexao.cursor()


# Apagar tabela
#cursor.execute("""
#    DELETE FROM coisas;
#""")

#-----------------------------------------

# Criar tabela
cursor.execute("""
    CREATE TABLE IF NOT EXISTS coisas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(100),
        qtd INTEGER DEFAULT 0
    )
""")

# Inserir um produto
cursor.execute(
    "INSERT INTO coisas (nome, qtd) VALUES (?, ?)",
    ("Mouse", 1) # Alterar
)

# Consultar os dados
cursor.execute("SELECT * FROM coisas")
dados = cursor.fetchall()

for linha in dados:
    print(linha)

# Salvar as alterações
conexao.commit()
conexao.close()

# --------------------------------
# Enviar o banco para o Kaggle
# --------------------------------

# Substitua pelo identificador do seu dataset
handle = "diogospeck/banco-teste"



enviar_dataset(handle, str(pasta))