import pandas as pd
import sqlite3
import os

CAMINHO_CSV = "covid_etl/dados_sus/dados_transformados.csv"
CAMINHO_DB = "covid_etl/dados_covid.db"
TABELA = "vacinacao"

def carregar_dados_no_sqlite():
    print("Lendo dados transformados...")
    df = pd.read_csv(CAMINHO_CSV)

    print("Criando banco SQLite e carregando dados...")
    conn = sqlite3.connect(CAMINHO_DB)
    df.to_sql(TABELA, conn, if_exists="replace", index=False)
    conn.close()
    print(f"Dados carregados no banco: {CAMINHO_DB}")

def executar_consultas():
    conn = sqlite3.connect(CAMINHO_DB)
    cursor = conn.cursor()

    print("\nConsulta 1: Média de idade por tipo de vacina")
    consulta1 = """
        SELECT vacina, ROUND(AVG(idade)) AS media_idade
        FROM vacinacao
        WHERE idade IS NOT NULL
        GROUP BY vacina
        ORDER BY media_idade DESC;
    """
    resultado1 = pd.read_sql_query(consulta1, conn)
    print(resultado1)

    print("\nConsulta 2: Quantidade de vacinas aplicadas por tipo")
    consulta2 = """
        SELECT vacina, COUNT(*) AS quantidade_aplicada
        FROM vacinacao
        GROUP BY vacina
        ORDER BY quantidade_aplicada DESC;
    """
    resultado2 = pd.read_sql_query(consulta2, conn)
    print(resultado2)

    conn.close()

if __name__ == "__main__":
    carregar_dados_no_sqlite()
    executar_consultas()
