import requests
import pandas as pd
import os
from datetime import datetime
from requests.auth import HTTPBasicAuth

url = "https://imunizacao-es.saude.gov.br/desc-imunizacao/_search"

# Diretório 
output_dir = "covid_etl/dados_sus"
os.makedirs(output_dir, exist_ok=True)

# Nome do arquivo com data da extração
hoje = datetime.today().strftime('%Y-%m-%d')
output_file = os.path.join(output_dir, f"imunizacao_dados_{hoje}.csv")

# Credenciais
usuario = "imunizacao_public"
senha = "qlto5t&7r_@+#Tlstigi"


payload = {
    "size": 1000 
}

def extrair_dados_covid():
    print("Iniciando extração dos dados da API do DataSUS...")
    response = requests.get(url, json=payload, auth=HTTPBasicAuth(usuario, senha))

    if response.status_code == 200:
        data = response.json()
        registros = [hit['_source'] for hit in data['hits']['hits']]
        df = pd.DataFrame(registros)
        df.to_csv(output_file, index=False, encoding="utf-8")
        print(f"✅ Dados salvos em: {output_file}")
    else:
        raise Exception(f"Erro ao acessar os dados. Status code: {response.status_code}")

if __name__ == "__main__":
    extrair_dados_covid()
