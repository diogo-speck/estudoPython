/* SQLite */
CREATE TABLE IF NOT EXISTS coisas(nome VARCHAR(100), qtd INT DEFAULT 0);
INSERT INTO coisas(nome, qtd)
VALUES ("Celular", 1);
SELECT *
FROM coisas;