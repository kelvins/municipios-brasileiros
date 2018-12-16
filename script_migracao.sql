CREATE TABLE estados(
    codigo_uf INT NOT NULL,
    uf VARCHAR(2) NOT NULL,
    nome VARCHAR(100) NOT NULL,
    PRIMARY KE (codigo_uf)
);

CREATE TABLE municipios(
    codigo_ibge INT NOT NULL,
    nome VARCHAR(100) NOT NULL,
    latitude FLOAT(8) NOT NULL,
    longitude FLOAT(8) NOT NULL,
    capital BOOLEAN NOT NULL,
    codigo_uf INT NOT NULL,
    PRIMARY KEY (codigo_ibge),
    FOREIGN KEY (codigo_uf) REFERENCES estado (codigo_uf)
);

INSERT INTO estados (codigo_uf, uf, nome) 
SELECT codigo_uf, uf, estado FROM municipios GROUP BY codigo_uf, uf, estado;

INSERT INTO municipios2 (codigo_ibge, nome, latitude, longitude, capital, codigo_uf) 
SELECT codigo_ibge, nome_municipio, latitude, longitude, capital, codigo_uf FROM municipios;

DROP TABLE municipios;

RENAME TABLE municipios2 TO municipios;
