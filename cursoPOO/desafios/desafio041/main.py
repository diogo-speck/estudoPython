import sqlite3
from datetime import datetime

"""
Adapte o código do exercício 18 para que a saída do script:
- Mostre uma mensagem caso não seja encontrado nenhum registro.
- Trate as datas inválidas e vazias.
- Mostre a data formatada corretamente.
- Mostre a idade real da pessoa.
"""

busca = input("Quem você procura? ").strip()


arquivo = "/home/diogospeck/Documents/Prog/estudoPython/sqluxo/sql/dataset/banco.db"

try:
    with sqlite3.connect(arquivo) as banco: # boas práticas para não precisar fechar no final
        banco.row_factory = sqlite3.Row # para nomear as linhas se necessário
        cur = banco.cursor()

        cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        #for n in cur:
        #    print(n[0])
        cur.execute("SELECT * FROM pragma_table_info('pessoas');")

        #for item in cur:
            #print(f"{item[0]}(cid) {item[1]}(name) {item[2]}(type) {item[3]}(notNull) {item[4]}(dflt_value) {item[5]}(pk)")

        
        total = 0
        cur.execute(f"SELECT * FROM pessoas WHERE 1=1 AND nome LIKE ? LIMIT 15", (f"%{busca}%",)) # invés de '%{busca}%' (sqlInjection)
        
        for total, item in enumerate(cur, start=1): # equivalente a fetchone() (ponteiro para uma tupla de cada vez)
            print(f"{item['id']} - {item['nome']} ", end="")
            try:
                data = datetime.strptime(item['data'], "%Y-%m-%d")
                if data > datetime.now():
                    raise ValueError
                idade = datetime.now().year-data.year
                if not (datetime.now().month > data.month or (datetime.now().month == data.month and datetime.now().day >= data.day)):
                    idade-=1
                print(f"nasceu em {datetime.strftime(data, '%d/%m/%Y')} e tem {(idade)} ano(s)")

            except ValueError:
                print("está com a Data Inválida")

        print(f"{("Nenhum registro encontrado" if total == 0 else f"{total} Item(s) encontrado(s)")}")


        cur.execute("CREATE TABLE IF NOT EXISTS pessoas(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), data TEXT STRICT)")

        ("""
        INSERT INTO pessoas (nome, data)
        VALUES('Mariazinha','2007-02-47')
        """)

except sqlite3.Error as erro:
    print(f"Falha no Banco de Dados: {erro}")

except Exception as erro:
    print(f"Erro: {erro}")