import os
import pandas as pd
from datetime import datetime
import win32com.client as win32
import shutil

def remove_protection(file_path, temp_folder):
    excel = win32.DispatchEx('Excel.Application')
    workbook = excel.Workbooks.Open(file_path)
    base_name = os.path.basename(file_path)
    new_file_path = os.path.join(temp_folder, base_name)
    workbook.SaveAs(new_file_path, FileFormat=51)  # FileFormat=51 is for .xlsx files
    workbook.Close(False)
    excel.Application.Quit()
    return new_file_path

def append_excel_files(input_folder, output_file):
    data_temp_folder = os.path.join(input_folder, 'data_temp')
    if not os.path.exists(data_temp_folder):
        os.makedirs(data_temp_folder)

    all_files = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.endswith('.xlsx')]
    data_frames = []

    for file in all_files:
        unprotected_file = remove_protection(file, data_temp_folder)
        df = pd.read_excel(unprotected_file)
        df.insert(0, 'ID', range(1, 1 + len(df)))
        df.insert(1, 'data_dados', datetime.now().strftime('%Y-%m-%d'))
        data_frames.append(df)

    final_df = pd.concat(data_frames, ignore_index=True)

    final_df.to_excel(output_file, index=False)

    # Apaga a pasta data_temp e todo o seu conteúdo
    shutil.rmtree(data_temp_folder)

