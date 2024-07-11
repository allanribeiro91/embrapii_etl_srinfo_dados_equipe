import os
import shutil
from glob import glob

def mover_arquivos_excel():

    downloads_folder = r'C:\Users\allan.ribeiro\Downloads'
    data_raw_folder = r'C:\Users\allan.ribeiro\OneDrive\Embrapii\ETL SRInfo Equipes\data_raw'

    # Verifica se a pasta data_raw existe, se não, cria
    if not os.path.exists(data_raw_folder):
        os.makedirs(data_raw_folder)

    # Exclui todos os arquivos existentes na pasta data_raw
    for file in os.listdir(data_raw_folder):
        file_path = os.path.join(data_raw_folder, file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f'Erro ao excluir {file_path}. Razão: {e}')

    # Lista todos os arquivos Excel na pasta Downloads
    files = glob(os.path.join(downloads_folder, '*.xlsx'))
    
    # Ordena os arquivos por data de modificação (mais recentes primeiro)
    files.sort(key=os.path.getmtime, reverse=True)
    
    # Seleciona os 3 arquivos mais recentes
    files_to_move = files[:3]
    
    # Move os arquivos selecionados para a pasta data_raw
    for file in files_to_move:
        shutil.move(file, data_raw_folder)


