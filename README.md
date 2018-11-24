# Municípios Brasileiros [![Build Status](https://travis-ci.org/kelvins/Municipios-Brasileiros.svg?branch=master)](https://travis-ci.org/kelvins/Municipios-Brasileiros)

Arquivos `SQL`, `CSV` e `JSON` contendo o código IBGE, nome do município, código UF, UF, estado, latitude e longitude de todos (ou quase todos) os municípios brasileiros. Total de 5.570 registros.

## Exemplos

| Código IBGE |  Nome do Município  | Código UF | UF |       Estado      | Capital | Latitude | Longitude |
|:-----------:|:-------------------:|:---------:|:--:|:-----------------:|:-------:|:--------:|:---------:|
|   5200050   | Abadia de Goiás     |     52    | GO | Goiás             |    0    | -16.7573 |  -49.4412 |
|   3100104   | Abadia dos Dourados |     31    | MG | Minas Gerais      |    0    | -18.4831 |  -47.3916 |
|   5200100   | Abadiânia           |     52    | GO | Goiás             |    0    | -16.1970 |  -48.7057 |
|   3100203   | Abaeté              |     31    | MG | Minas Gerais      |    0    | -19.1551 |  -45.4444 |
|   4314902   | Porto Alegre        |     43    | RS | Rio Grande do Sul |    1    | -30.0318 |  -51.2065 |

### Exemplo SQL

```sql
CREATE TABLE municipios(
       codigo_ibge INT NOT NULL,
       nome_municipio VARCHAR(100) NOT NULL,
       codigo_uf INT NOT NULL,
       uf VARCHAR(2) NOT NULL,
       estado VARCHAR(100) NOT NULL,
       capital BOOLEAN NOT NULL,
       latitude FLOAT(8) NOT NULL,
       longitude FLOAT(8) NOT NULL,
       PRIMARY KEY(codigo_ibge)
);

INSERT INTO municipios VALUES
(5200050, 'Abadia de Goiás', 52, 'GO', 'Goiás', FALSE, -16.7573, -49.4412),
(3100104, 'Abadia dos Dourados', 31, 'MG', 'Minas Gerais', FALSE, -18.4831, -47.3916),
(5200100, 'Abadiânia', 52, 'GO', 'Goiás', FALSE, -16.197, -48.7057),
(3100203, 'Abaeté', 31, 'MG', 'Minas Gerais', FALSE, -19.1551, -45.4444),
(1500107, 'Abaetetuba', 15, 'PA', 'Pará', FALSE, -1.72183, -48.8788),
(2300101, 'Abaiara', 23, 'CE', 'Ceará', FALSE, -7.34588, -39.0416),
(2900108, 'Abaíra', 29, 'BA', 'Bahia', FALSE, -13.2488, -41.6619),
(2900207, 'Abaré', 29, 'BA', 'Bahia', FALSE, -8.72073, -39.1162),
(4100103, 'Abatiá', 41, 'PR', 'Paraná', FALSE, -23.3049, -50.3133),
...
```

### Exemplo CSV

```csv
codigo_ibge,nome_municipio,codigo_uf,uf,estado,capital,latitude,longitude
5200050,Abadia de Goiás,52,GO,Goiás,0,-16.7573,-49.4412
3100104,Abadia dos Dourados,31,MG,Minas Gerais,0,-18.4831,-47.3916
5200100,Abadiânia,52,GO,Goiás,0,-16.197,-48.7057
3100203,Abaeté,31,MG,Minas Gerais,0,-19.1551,-45.4444
1500107,Abaetetuba,15,PA,Pará,0,-1.72183,-48.8788
2300101,Abaiara,23,CE,Ceará,0,-7.34588,-39.0416
2900108,Abaíra,29,BA,Bahia,0,-13.2488,-41.6619
2900207,Abaré,29,BA,Bahia,0,-8.72073,-39.1162
4100103,Abatiá,41,PR,Paraná,0,-23.3049,-50.3133
```

### Exemplo JSON

```json
[
  {
    "codigo_ibge" : 5200050,
    "nome_municipio" : "Abadia de Goiás",
    "codigo_uf" : 52,
    "uf" : "GO",
    "estado" : "Goiás",
    "capital" : false,
    "latitude" : -16.7573,
    "longitude" : -49.4412
  },
  {
    "codigo_ibge" : 3100104,
    "nome_municipio" : "Abadia dos Dourados",
    "codigo_uf" : 31,
    "uf" : "MG",
    "estado" : "Minas Gerais",
    "capital" : false,
    "latitude" : -18.4831,
    "longitude" : -47.3916
  }
]
```

**Nota**: caso encontre qualquer dado inconsistente ou tenha alguma sugestão por favor crie uma [issue](https://github.com/kelvins/Municipios-Brasileiros/issues) ou envie um [pull request](https://github.com/kelvins/Municipios-Brasileiros/pulls) diretamente. Obrigado a todos os [colaboradores](https://github.com/kelvins/Municipios-Brasileiros/graphs/contributors). :raised_hands:

## Exportação dos Dados

Existem diversas ferramentas para trabalhar com bancos de dados e exportar os dados em outros formatos como `CSV`, `JSON`, entre outros.
Uma ferramenta que costumo utilizar com frequência é o [DBeaver](https://dbeaver.io/), pois além de ser multiplataforma ela é simples de usar e disponibiliza vários opções para a exportação dos dados.

## Queries Úteis

- Mostra todas as capitais ordenando por estado:

  ```sql
  SELECT estado, uf, nome_municipio as 'capital' FROM municipios WHERE capital = TRUE ORDER BY estado;
  ```

- Mostra todos os municípios de um estado específico ordenando por nome do município:

  ```sql
  SELECT * FROM municipios WHERE uf = 'RS' ORDER BY nome_municipio;
  ```

- Mostra os registros de uma determinada região (latitude e longitude):

  ```sql
  SELECT * FROM municipios WHERE latitude >= -32.0000 AND latitude <= -27.0000 AND longitude >= -55.0000 AND longitude <= -50.0000;
  ```
