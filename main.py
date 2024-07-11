from append_arquivos import append_excel_files
from tabela_pessoa import criar_tabela_pessoa
from tabela_pessoa_vinculo_ue import criar_tabela_pessoa_vinculo_ue

def etl_srinfo_equipes():
    input_folder = r'C:\Users\allan.ribeiro\OneDrive\Embrapii\ETL SRInfo Equipes\data_raw'
    output_file = r'C:\Users\allan.ribeiro\OneDrive\Embrapii\ETL SRInfo Equipes\data_processed\srinfo_equipe_ues.xlsx'
    append_excel_files(input_folder, output_file)
    print('Join de arquivos realizado com sucesso!')

    caminho_arquivo = r'C:\Users\allan.ribeiro\OneDrive\Embrapii\ETL SRInfo Equipes\data_processed\srinfo_equipe_ues.xlsx'
    criar_tabela_pessoa(caminho_arquivo)
    print('tabela_pessoa criada!')

    criar_tabela_pessoa_vinculo_ue(caminho_arquivo)
    print('tabela_pessoa_vinculo_ue criada!')

if __name__ == "__main__":
    etl_srinfo_equipes()
