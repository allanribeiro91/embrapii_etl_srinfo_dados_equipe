from datetime import datetime
from baixar_dados import baixar_dados
from mover_arquivos import mover_arquivos_excel
from append_arquivos import append_excel_files
from tabela_pessoa import criar_tabela_pessoa
from tabela_pessoa_vinculo_ue import criar_tabela_pessoa_vinculo_ue
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

def etl_srinfo_equipes():

    username = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')
    sharepoint_site_url = os.getenv('SHAREPOINT_SITE')
    sharepoint_folder = os.getenv('SHAREPOINT_FOLDER')
    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')
    tenant_id = os.getenv('TENANT_ID')

    print('Data/hora de início: ', datetime.now().strftime('%d/%m/%y %H:%M:%S'))

    # baixar_dados(username, password)

    # mover_arquivos_excel()
    print("Arquivos movidos com sucesso!")

    # append_excel_files()
    print('Join de arquivos realizado com sucesso!')

    caminho_arquivo = r'C:\Users\allan.ribeiro\OneDrive\Embrapii\ETL SRInfo Equipes\data_processed\srinfo_equipe_ues.xlsx'
    criar_tabela_pessoa(caminho_arquivo)
    print('tabela_pessoa criada!')

    criar_tabela_pessoa_vinculo_ue(caminho_arquivo)
    print('tabela_pessoa_vinculo_ue criada!')

    print('Data/hora de fim: ', datetime.now().strftime('%d/%m/%y %H:%M:%S'))

if __name__ == "__main__":
    etl_srinfo_equipes()
