-- SQL: Structured Query Language / Linguagem de Consulta
/* Dar uma olhada em SQLAlchemy, PostgreSQL e azure data studio
MSSQL
*/
GO
IF DB_ID('meu_banco_de_tras') IS NULL -- Se o banco de dados não existir, cria um novo banco de dados
BEGIN
CREATE DATABASE meu_banco_de_tras;
END;

GO
USE meu_banco_de_tras; -- Usa o banco de dados criado

GO
DROP TABLE IF EXISTS pessoas; -- Deleta a tabela pessoas caso ela exista para atualizar

GO
IF OBJECT_ID('dbo.pessoas', 'U') IS NULL -- Verifica se a tabela já existe
BEGIN -- Se existe, sempre existe nesse caso, cria uma nova tabela
    CREATE TABLE pessoas (
        id INT IDENTITY(1,1) PRIMARY KEY, -- Separador de dados que adiciona auto incremento na coluna id
        nome  VARCHAR (100), -- Limite de 100 caracteres
        email VARCHAR (100)
    );
END;

GO
INSERT  INTO pessoas (nome, email)
VALUES ('Diogo', 'diogospeck@gmail.com');
GO
INSERT  INTO pessoas (nome, email)
VALUES ('João', 'joao@gmail.com');
GO
INSERT  INTO pessoas (nome, email)
VALUES ('Maria', 'maria@gmail.com');


GO
SELECT *
FROM   pessoas

GO
IF OBJECT_ID('dbo.produtos', 'U') IS NULL -- Verifica se a tabela já existe
BEGIN -- Se existe, sempre existe nesse caso, cria uma nova tabela
    CREATE TABLE produtos (
        id INT IDENTITY(1,1) PRIMARY KEY, -- Separador de dados que adiciona auto incremento na coluna id
        item  VARCHAR (100),
        preco DECIMAL (6,2) -- 9999,99
    );
END;
ELSE
INSERT  INTO produtos (item, preco)
VALUES ('Água', 5.00); -- Adiciona um item na tabela produtos

/*
DELETE FROM produtos -- Apaga tudo
*/

GO
UPDATE produtos
SET preco = 6.00
WHERE item = 'Água' -- Atualiza o preço do item Água

GO
SELECT *
FROM   produtos
WHERE item = 'Água'