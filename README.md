# Municípios Brasileiros

Arquivo SQL contendo o código IBGE, nome do município, código UF, UF, estado, latitude e longitude.

**Exemplo**:

| Código IBGE |  Nome do Município  | Código UF | UF |    Estado    | Latitude | Longitude |
|:-----------:|:-------------------:|:---------:|:--:|:------------:|:--------:|:---------:|
|   5200050   | Abadia de Goiás     |     52    | GO | Goiás        | -16.7573 |  -49.4412 |
|   3100104   | Abadia dos Dourados |     31    | MG | Minas Gerais | -18.4831 |  -47.3916 |
|   5200100   | Abadiânia           |     52    | GO | Goiás        |  -16.197 |  -48.7057 |
|   3100203   | Abaeté              |     31    | MG | Minas Gerais | -19.1551 |  -45.4444 |

**SQL**:
```sql
(5200050, "Abadia de Goiás", 52, "GO", "Goiás", -16.7573, -49.4412),
(3100104, "Abadia dos Dourados", 31, "MG", "Minas Gerais", -18.4831, -47.3916),
(5200100, "Abadiânia", 52, "GO", "Goiás", -16.197, -48.7057),
(3100203, "Abaeté", 31, "MG", "Minas Gerais", -19.1551, -45.4444),
(1500107, "Abaetetuba", 15, "PA", "Pará", -1.72183, -48.8788),
(2300101, "Abaiara", 23, "CE", "Ceará", -7.34588, -39.0416),
(2900108, "Abaíra", 29, "BA", "Bahia", -13.2488, -41.6619),
(2900207, "Abaré", 29, "BA", "Bahia", -8.72073, -39.1162),
(4100103, "Abatiá", 41, "PR", "Paraná", -23.3049, -50.3133),
```

**Atenção**: utilizei dados de 3 tabelas diferentes, então podem haver dados inconsistentes. Caso encontre algum sinta-se à vontade para submeter um pull request ou criar um issue.
