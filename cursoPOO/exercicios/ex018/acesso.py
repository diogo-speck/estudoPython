import sqlite3


busca = input("O que você procura? ").strip()




# Caminho do banco SQLite
arquivo = "/home/diogospeck/Documents/Prog/estudoPython/sqluxo/sql/dataset/banco.db"

# Conectar ao banco

try:
    with sqlite3.connect(arquivo) as banco: # boas práticas para não precisar fechar no final
        banco.row_factory = sqlite3.Row # para nomear as linhas se necessário
        cur = banco.cursor()


        # Consultar as tabelas dos dados
        cur.execute("SELECT name FROM sqlite_master WHERE type='table';")

        # Consultar o nome dos atributos na tabela coisas
        cur.execute("SELECT * FROM pragma_table_info('coisas');")

        #for item in cur:
        #    print(f"{item[0]}(cid) {item[1]}(name) {item[2]}(type) {item[3]}(notNull) {item[4]}(dflt_value) {item[5]}(pk)")

        cur.execute("SELECT * FROM coisas")

        # dados = cur.fetchall() retorna cópias das tuplas

        #print(dados)
        
        total = 0
        cur.execute(f"SELECT * FROM coisas WHERE nome LIKE ?", (f"%{busca}%",)) # invés de '%{busca}%' (sqlInjection)
        
        for total, item in enumerate(cur, start=1): # equivalente a fetchone() (ponteiro para uma tupla de cada vez)
            print(f"{item['qtd']} - {item['nome']}")

        print(f"[{total}] Item(s) encontrado(s)") # invés do enum start = 1 (0 if total == 0 else total+1)


except sqlite3.Error as erro:
    print(f"Falha no Banco de Dados: {erro}")

except Exception as erro:
    print(f"Erro: {erro}")


#cur.close()
#banco.close()