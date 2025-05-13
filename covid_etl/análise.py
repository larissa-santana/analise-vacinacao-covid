import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Configuração dos gráficos
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

CAMINHO_DB = "covid_etl/dados_covid.db"
TABELA = "vacinacao"

def carregar_dados():
    conn = sqlite3.connect(CAMINHO_DB)
    df = pd.read_sql_query(f"SELECT * FROM {TABELA}", conn)
    conn.close()
    return df

def grafico_idade_por_vacina(df):
    plt.figure()
    sns.boxplot(data=df, x="vacina", y="idade")
    plt.title("Distribuição da idade por tipo de vacina")
    plt.xlabel("Vacina")
    plt.ylabel("Idade")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("covid_etl/grafico_idade_por_vacina.png")
    plt.show()

def grafico_quantidade_vacinas(df):
    plt.figure()
    vacinas = df["vacina"].value_counts().reset_index()
    vacinas.columns = ["vacina", "quantidade"]
    sns.barplot(data=vacinas, x="vacina", y="quantidade", palette="viridis")
    plt.title("Quantidade de doses aplicadas por tipo de vacina")
    plt.xlabel("Vacina")
    plt.ylabel("Quantidade")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("covid_etl/grafico_qtd_vacinas.png")
    plt.show()

def grafico_media_idade_por_estado(df):
    plt.figure(figsize=(12, 6))

    # Filtra os 10 estados com mais registros
    estados_mais_frequentes = df['estado'].value_counts().nlargest(10).index
    df_filtrado = df[df['estado'].isin(estados_mais_frequentes)]

    # Calcula a média de idade por estado
    media_idade = df_filtrado.groupby("estado")["idade"].mean().sort_values(ascending=False)

    # Plota gráfico de barras
    sns.barplot(x=media_idade.index, y=media_idade.values, palette="viridis")
    plt.title("Média de idade por estado (Top 10)")
    plt.xlabel("Estado")
    plt.ylabel("Média de Idade")
    plt.ylim(0, df['idade'].max() + 5)
    plt.tight_layout()
    plt.savefig("covid_etl/grafico_media_idade_por_estado.png")
    plt.show()


def main():
    print("📊 Carregando dados do banco...")
    df = carregar_dados()

    print("🔍 Exibindo análises...")
    grafico_idade_por_vacina(df)
    grafico_quantidade_vacinas(df)
    grafico_media_idade_por_estado(df)

    print("✅ Análises finalizadas. Gráficos salvos na pasta covid_etl/")

if __name__ == "__main__":
    main()
