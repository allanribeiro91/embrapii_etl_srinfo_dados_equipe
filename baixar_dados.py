import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService

# Carregar variáveis do arquivo .env
load_dotenv()
SENHA = os.getenv('SENHA')

def baixar_dados():
    # Configurar o WebDriver usando webdriver-manager
    edge_service = EdgeService(EdgeChromiumDriverManager().install())
    options = webdriver.EdgeOptions()
    # options.add_argument('--headless') 
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('start-maximized')
    options.add_argument('disable-infobars')
    options.add_argument('--disable-extensions')

    driver = webdriver.Edge(service=edge_service, options=options)
    
    try:
        # 1. Entrar no link
        driver.get('https://srinfo.embrapii.org.br/users/login/')
        time.sleep(5)
        
        # username e senha
        username_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'id_username'))
        )
        username_field.send_keys("allan.ribeiro")
        
        password_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'password'))
        )
        password_field.send_keys(SENHA)


        # 2. Clicar em "btn-primary"
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'btn-primary'))
        )
        login_button.click()

        # 3. Esperar 2 segundos
        time.sleep(3)

        # 4. Ir para o link da lista de pessoas
        driver.get('https://srinfo.embrapii.org.br/people/list/')
        
        # 5. Selecionar "9999" no dropdown
        dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'form-control.input-sm'))
        )
        dropdown.click()
        option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//option[@value='9999']"))
        )
        option.click()

        # 6. Esperar 60 segundos para carregar
        time.sleep(2)
        print('Esperando carregar dados... Página 01')
        WebDriverWait(driver, 90).until(
            EC.invisibility_of_element_located((By.ID, 'object-list_processing'))
        )
        time.sleep(2)

        # 7. Clicar em "buttons-excel"
        excel_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'buttons-excel'))
        )
        excel_button.click()

        # 8. Esperar 3 segundos
        time.sleep(3)

        # Repetir para as páginas 2 e 3
        for page_number in [3, 4]:
            # 9. Clicar na página seguinte
            next_page = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"//*[@id='object-list_paginate']/ul/li[{page_number}]/a"))
            )
            next_page.click()

            # 10. Esperar 20 segundos para carregar os dados
            time.sleep(2)
            print(f'Esperando carregar dados...  Página 0{page_number -1}')
            WebDriverWait(driver, 90).until(
                EC.invisibility_of_element_located((By.ID, 'object-list_processing'))
            )
            time.sleep(2)

            # 11. Clicar em "buttons-excel"
            excel_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'buttons-excel'))
            )
            excel_button.click()

            # 12. Esperar 3 segundos
            time.sleep(3)

        print("Download de dados concluído!")
        time.sleep(3)
    finally:
        driver.quit()

if __name__ == "__main__":
    baixar_dados()