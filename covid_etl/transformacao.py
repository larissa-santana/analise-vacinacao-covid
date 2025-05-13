import os
import pandas as pd
from datetime import datetime

DIRETORIO_DADOS = "covid_etl/dados_sus"


colunas_interesse = [
    "paciente_idade", 
    "paciente_enumsexo", 
    "estabelecimento_uf", 
    "vacina_nome", 
    "vacina_fabricante_nome", 
    "vacina_dataAplicacao"
]

def buscar_csv_mais_recente(diretorio):
    arquivos_csv = [f for f in os.listdir(diretorio) if f.endswith(".csv")]
    if not arquivos_csv:
        raise FileNotFoundError("Nenhum arquivo CSV encontrado na pasta.")
    
    arquivos_ordenados = sorted(
        arquivos_csv,
        key=lambda x: os.path.getmtime(os.path.join(diretorio, x)),
        reverse=True
    )
    return os.path.join(diretorio, arquivos_ordenados[0])

def transformar_dados(df):
    print("Transformando dados...")

    
    colunas_faltando = [col for col in colunas_interesse if col not in df.columns]
    if colunas_faltando:
        print(f"Atenção: As seguintes colunas não foram encontradas no CSV e serão ignoradas: {colunas_faltando}")
    
    colunas_validas = [col for col in colunas_interesse if col in df.columns]
    df = df[colunas_validas]

   
    df.rename(columns={
        "paciente_idade": "idade",
        "paciente_enumsexo": "sexo",
        "estabelecimento_uf": "estado",
        "vacina_nome": "vacina",
        "vacina_fabricante_nome": "fabricante",
        "vacina_dataAplicacao": "data_aplicacao"
    }, inplace=True)

    
   
    if "data_aplicacao" in df.columns:
        df["data_aplicacao"] = pd.to_datetime(df["data_aplicacao"], errors='coerce')

    return df

def pipeline():
    print("Buscando arquivo mais recente...")
    caminho_csv = buscar_csv_mais_recente(DIRETORIO_DADOS)
    print(f"Lendo dados de: {caminho_csv}")
    
    df = pd.read_csv(caminho_csv)
    df_transformado = transformar_dados(df)

    
    nome_saida = "dados_transformados.csv"
    caminho_saida = os.path.join(DIRETORIO_DADOS, nome_saida)
    df_transformado.to_csv(caminho_saida, index=False)
    print(f"Dados transformados salvos em: {caminho_saida}")

if __name__ == "__main__":
    pipeline()
