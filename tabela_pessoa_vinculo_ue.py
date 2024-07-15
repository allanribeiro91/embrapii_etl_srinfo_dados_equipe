import pandas as pd
import os
from datetime import datetime
from mover_para_sharepoint import mover_para_sharepoint

def criar_tabela_pessoa_vinculo_ue(caminho_arquivo):
    # Carrega o arquivo Excel
    df = pd.read_excel(caminho_arquivo)

    # Seleciona e renomeia as colunas necessárias
    df = df[['CPF', 'Unidade EMBRAPII', 'Titulação', 'Formação Acadêmica', 'Atividade / Função', 'Disponibilidade (horas/mês)', 'Data de entrada', 'Data de saída']]
    df.columns = ['cpf', 'ue', 'titulacao', 'formacao_academica', 'atividade_funcao', 'disponibilidade_horas_mes', 'data_entrada', 'data_saida']

    # Adiciona a coluna data_dados com a data atual
    df['data_dados'] = datetime.now().strftime('%Y-%m-%d')

    # Converte as colunas de data para o tipo datetime
    df['data_entrada'] = pd.to_datetime(df['data_entrada'], errors='coerce')
    df['data_saida'] = pd.to_datetime(df['data_saida'], errors='coerce')
    df['data_dados'] = pd.to_datetime(df['data_dados'], errors='coerce')

    # Salva o resultado em um novo arquivo Excel
    output_file = r'data_processed/tabela_pessoa_vinculo_ue.xlsx'
    df.to_excel(output_file, index=False)

    # Mover para SharePoint
    mover_para_sharepoint(output_file)