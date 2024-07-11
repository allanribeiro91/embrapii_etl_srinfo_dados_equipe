from datetime import datetime
from baixar_dados import baixar_dados
from mover_arquivos import mover_arquivos_excel
from append_arquivos import append_excel_files
from tabela_pessoa import criar_tabela_pessoa
from tabela_pessoa_vinculo_ue import criar_tabela_pessoa_vinculo_ue

def etl_srinfo_equipes():

    print('Data/hora de início: ', datetime.now().strftime('%d/%m/%y %H:%M:%S'))

    baixar_dados()

    mover_arquivos_excel()
    print("Arquivos movidos com sucesso!")

    append_excel_files()
    print('Join de arquivos realizado com sucesso!')

    caminho_arquivo = r'C:\Users\allan.ribeiro\OneDrive\Embrapii\ETL SRInfo Equipes\data_processed\srinfo_equipe_ues.xlsx'
    criar_tabela_pessoa(caminho_arquivo)
    print('tabela_pessoa criada!')

    criar_tabela_pessoa_vinculo_ue(caminho_arquivo)
    print('tabela_pessoa_vinculo_ue criada!')

    print('Data/hora de fim: ', datetime.now().strftime('%d/%m/%y %H:%M:%S'))

if __name__ == "__main__":
    etl_srinfo_equipes()
