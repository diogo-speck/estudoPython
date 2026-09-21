-- SQL: Structured Query Language / Linguagem de Consulta
/* Dar uma olhada em SQLAlchemy, PostgreSQL e azure data studio
MSSQL
*/
CREATE DATABASE meu_banco_de_tras;
GO
USE meu_banco_de_tras;
GO
CREATE TABLE pessoas (
    id    INT           PRIMARY KEY, -- Separador de dados
    nome  VARCHAR (100), -- Limite de 100 caracteres
    email VARCHAR (100)
);
GO
INSERT  INTO pessoas (id, nome, email)
VALUES (1, 'Diogo', 'diogospeck@gmail.com');
GO
SELECT *
FROM   pessoas
WHERE  id = 1;