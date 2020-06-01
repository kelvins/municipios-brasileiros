# Municípios Brasileiros [![Build Status](https://travis-ci.org/kelvins/Municipios-Brasileiros.svg?branch=master)](https://travis-ci.org/kelvins/Municipios-Brasileiros)

Arquivos `SQL`, `CSV` e `JSON` contendo o código IBGE, nome do município, capital, código UF, UF, estado, latitude e longitude de todos (ou quase todos) os municípios brasileiros. Total de 5.570 registros.

## Exemplos

### Dados

| Código IBGE |  Nome do Município  | Código UF | UF |       Estado      | Capital | Latitude | Longitude |
|:-----------:|:-------------------:|:---------:|:--:|:-----------------:|:-------:|:--------:|:---------:|
|   5200050   | Abadia de Goiás     |     52    | GO | Goiás             |    0    | -16.7573 |  -49.4412 |
|   3100104   | Abadia dos Dourados |     31    | MG | Minas Gerais      |    0    | -18.4831 |  -47.3916 |
|   5200100   | Abadiânia           |     52    | GO | Goiás             |    0    | -16.1970 |  -48.7057 |
|   3100203   | Abaeté              |     31    | MG | Minas Gerais      |    0    | -19.1551 |  -45.4444 |
|   4314902   | Porto Alegre        |     43    | RS | Rio Grande do Sul |    1    | -30.0318 |  -51.2065 |

### Exemplo SQL

#### Estados

```sql
CREATE TABLE estados(
    codigo_uf INT NOT NULL,
    uf VARCHAR(2) NOT NULL,
    nome VARCHAR(100) NOT NULL,
    latitude FLOAT(8) NOT NULL,
    longitude FLOAT(8) NOT NULL,
    PRIMARY KEY (codigo_uf)
);

INSERT INTO estados VALUES
(11,'RO','Rondônia',-10.83,-63.34),
(12,'AC','Acre',-8.77,-70.55),
(13,'AM','Amazonas',-3.47,-65.1),
...
```

#### Municípios

```sql
CREATE TABLE municipios(
    codigo_ibge INT NOT NULL,
    nome VARCHAR(100) NOT NULL,
    latitude FLOAT(8) NOT NULL,
    longitude FLOAT(8) NOT NULL,
    capital BOOLEAN NOT NULL,
    codigo_uf INT NOT NULL,
    PRIMARY KEY (codigo_ibge),
    FOREIGN KEY (codigo_uf) REFERENCES estados (codigo_uf)
);

INSERT INTO municipios VALUES
(5200050, 'Abadia de Goiás', -16.7573, -49.4412, FALSE, 52),
(3100104, 'Abadia dos Dourados', -18.4831, -47.3916, FALSE, 31),
(5200100, 'Abadiânia', -16.197, -48.7057, FALSE, 52),
...
```

### Exemplo CSV

#### Estados

```csv
codigo_uf,uf,nome
11,RO,Rondônia,-10.83,-63.34
12,AC,Acre,-8.77,-70.55
13,AM,Amazonas,-3.47,-65.1
...
```

#### Municípios

```csv
codigo_ibge,nome,latitude,longitude,capital,codigo_uf
5200050,Abadia de Goiás,-16.7573,-49.4412,0,52
3100104,Abadia dos Dourados,-18.4831,-47.3916,0,31
5200100,Abadiânia,-16.197,-48.7057,0,52
...
```

### Exemplo JSON

#### Estados

```json
[
  {
    "codigo_uf": 11,
    "uf": "RO",
    "nome": "Rondônia",
    "latitude": -10.83,
    "longitude": -63.34
  },
  {
    "codigo_uf": 12,
    "uf": "AC",
    "nome": "Acre",
    "latitude": -8.77,
    "longitude": -70.55
  },
  {
    "codigo_uf": 13,
    "uf": "AM",
    "nome": "Amazonas",
    "latitude": -3.47,
    "longitude": -65.1
  }
]
```

#### Municípios

```json
[
  {
    "codigo_ibge" : 5200050,
    "nome" : "Abadia de Goiás",
    "latitude" : -16.7573,
    "longitude" : -49.4412,
    "capital" : false,
    "codigo_uf" : 52
  },
  {
    "codigo_ibge" : 3100104,
    "nome" : "Abadia dos Dourados",
    "latitude" : -18.4831,
    "longitude" : -47.3916,
    "capital" : false,
    "codigo_uf" : 31
  },
  {
    "codigo_ibge" : 5200100,
    "nome" : "Abadiânia",
    "latitude" : -16.197,
    "longitude" : -48.7057,
    "capital" : false,
    "codigo_uf" : 52
  }
]
```

**Nota**: caso encontre qualquer dado inconsistente ou tenha alguma sugestão por favor crie uma [issue](https://github.com/kelvins/Municipios-Brasileiros/issues) ou envie um [pull request](https://github.com/kelvins/Municipios-Brasileiros/pulls) diretamente. Obrigado a todos os [colaboradores](https://github.com/kelvins/Municipios-Brasileiros/graphs/contributors). :raised_hands:

## Exportação dos Dados

Existem diversas ferramentas para trabalhar com bancos de dados e exportar os dados em outros formatos como `CSV`, `JSON`, entre outros.
Uma ferramenta que costumo utilizar com frequência é o [DBeaver](https://dbeaver.io/), pois além de ser multiplataforma ela é simples de usar e disponibiliza várias opções para a exportação dos dados.

## Serviço de Dados do IBGE

Hoje o IBGE conta com um serviço de dados que disponibiliza diversas informações sobre as localidades do Brasil.

A API do IBGE pode ser acessada pelo seguinte endereço: https://servicodados.ibge.gov.br/api/docs/localidades
