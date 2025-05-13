# 📊 Análise da Vacinação contra COVID-19 no Brasil

Projeto de ETL e análise exploratória utilizando dados públicos da API do DataSUS.

## 🔍 Objetivo

Automatizar a coleta, transformar e analisar os dados de vacinação contra a COVID-19 no Brasil, com foco em entender:
- A distribuição de idade por vacina
- A média de idade por tipo de estado
- A quantidade de aplicações por fabricante

## 🛠 Tecnologias

- Python
- Pandas
- SQLite
- Seaborn / Matplotlib
- Git / GitHub

## 📂 Estrutura do Projeto

covid_etl/
├── dados_sus/
│ └── dados_transformados.csv
├── dados_covid.db
├── extracao_api_sus.py
├── transformacao.py
├── consultas_sqlite.py
├── analise.py
└── gráficos PNG


## 📌 Scripts

- `extracao_api_sus.py`: Faz a requisição à API do DataSUS
- `transformacao.py`: Limpa e prepara os dados
- `consultas_sqlite.py`: Carrega dados no SQLite e faz consultas SQL
- `analise.py`: Baseados nos dados inseridos no SQLite, gera gráficos e análises com Seaborn/Matplotlib

## 📈 Exemplos de Gráficos

- Distribuição de idade por vacina
- Vacinas mais aplicadas
- Média de idade por estado

## 🔗 Fonte de Dados

[DataSUS OpenData](https://opendatasus.saude.gov.br/)

---

Feito por [Larissa Santana](https://www.linkedin.com/in/larissaliradesantana/)
