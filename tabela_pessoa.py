import pandas as pd
import os

def criar_tabela_pessoa(caminho_arquivo):
    # Verifica se o arquivo existe antes de tentar abrir
    if not os.path.exists(caminho_arquivo):
        print(f"Arquivo não encontrado: {caminho_arquivo}")
        return

    # Carrega o arquivo Excel
    df = pd.read_excel(caminho_arquivo)

    # Seleciona as colunas necessárias
    df = df[['data_dados', 'Nome', 'CPF', 'Link Lattes']]

    # Remove duplicatas com base na coluna 'CPF'
    df = df.drop_duplicates(subset=['CPF'])

    # Renomeia as colunas
    df.columns = ['data_dados', 'nome', 'cpf', 'lattes']

    # Reordena as colunas conforme solicitado
    df = df[['cpf', 'nome', 'lattes', 'data_dados']]

    # Converte a coluna data_dados para o tipo datetime
    df['data_dados'] = pd.to_datetime(df['data_dados'], errors='coerce')

    # Salva o resultado em um novo arquivo Excel
    output_path = 'data_processed/tabela_pessoa.xlsx'
    df.to_excel(output_path, index=False)
