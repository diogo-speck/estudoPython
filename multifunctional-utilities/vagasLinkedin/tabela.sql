CREATE TABLE vagas (
    id INTEGER PRIMARY KEY,
    url TEXT UNIQUE,
    empresa TEXT,
    cargo TEXT,
    data TEXT,
    easy_apply INTEGER,
    processada INTEGER
);