from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.client_credential import ClientCredential
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Variáveis de ambiente
SHAREPOINT_SITE = os.getenv('SHAREPOINT_SITE')
SHAREPOINT_FOLDER = os.getenv('SHAREPOINT_FOLDER')
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
TENANT_ID = os.getenv('TENANT_ID')

def mover_para_sharepoint(local_path):
    try:
        ctx = ClientContext(SHAREPOINT_SITE).with_credentials(ClientCredential(CLIENT_ID, CLIENT_SECRET))
        target_folder = ctx.web.get_folder_by_server_relative_url(SHAREPOINT_FOLDER)
        
        with open(local_path, 'rb') as content_file:
            file_content = content_file.read()
            
        target_folder.upload_file(os.path.basename(local_path), file_content).execute_query()
        print(f"Arquivo {local_path} movido para {SHAREPOINT_FOLDER} com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    
