# Municípios Brasileiros

Arquivos `SQL` e `CSV` contendo o código IBGE, nome do município, código UF, UF, estado, latitude e longitude de todos (ou quase todos) os municípios brasileiros. Total de 5.562 registros.

**Exemplo**:

| Código IBGE |  Nome do Município  | Código UF | UF |    Estado    | Latitude | Longitude |
|:-----------:|:-------------------:|:---------:|:--:|:------------:|:--------:|:---------:|
|   5200050   | Abadia de Goiás     |     52    | GO | Goiás        | -16.7573 |  -49.4412 |
|   3100104   | Abadia dos Dourados |     31    | MG | Minas Gerais | -18.4831 |  -47.3916 |
|   5200100   | Abadiânia           |     52    | GO | Goiás        | -16.1970 |  -48.7057 |
|   3100203   | Abaeté              |     31    | MG | Minas Gerais | -19.1551 |  -45.4444 |

**SQL**:
```sql
(5200050, "Abadia de Goiás", 52, "GO", "Goiás", -16.7573, -49.4412),
(3100104, "Abadia dos Dourados", 31, "MG", "Minas Gerais", -18.4831, -47.3916),
(5200100, "Abadiânia", 52, "GO", "Goiás", -16.1970, -48.7057),
(3100203, "Abaeté", 31, "MG", "Minas Gerais", -19.1551, -45.4444),
(1500107, "Abaetetuba", 15, "PA", "Pará", -1.72183, -48.8788),
(2300101, "Abaiara", 23, "CE", "Ceará", -7.34588, -39.0416),
(2900108, "Abaíra", 29, "BA", "Bahia", -13.2488, -41.6619),
(2900207, "Abaré", 29, "BA", "Bahia", -8.72073, -39.1162),
(4100103, "Abatiá", 41, "PR", "Paraná", -23.3049, -50.3133),
```

**Obs.**: o arquivo `CSV` foi gerado utilizando o **OpenOffice Calc** e codificação **UTF-8**.

**Nota**: caso encontre qualquer dado inconsistente por favor crie um issue ou envie um pull request diretamente.
