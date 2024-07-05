from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import openpyxl

driver = webdriver.Chrome()
# 1 – Navegar até o site https://contabilidade-devaprender.netlify.app/
driver.get('https://contabilidade-devaprender.netlify.app/')
sleep(5)
# 2 – Digitar e-mail
email = driver.find_element(By.XPATH,"//input[@id='email']")
sleep(2)
email.send_keys('admin@contabilidade.com')
# 3 – Digitar a senha
senha = driver.find_element(By.XPATH,"//input[@id='senha']")
sleep(2)
senha.send_keys('contabilidade123456')
# 4 – Clicar em entrar
botao_entrar = driver.find_element(By.XPATH,"//button[@id='Entrar']")

botao_entrar.click()

sleep(5)
# 5 - Extrair as informações da planilha
empresas = openpyxl.load_workbook('./empresas.xlsx')
pagina_empresas = empresas['dados empresas']
# 6 – Clicar em cada campo e preencher 
for linha in pagina_empresas.iter_rows(min_row=2,values_only=True):
    nome_empresa, email, telefone, endereco, cnpj, area_atuacao, quantidade_de_funcionarios, data_fundacao = linha

    driver.find_element(By.ID,'nomeEmpresa').send_keys(nome_empresa)
    sleep(1)
    driver.find_element(By.ID,'emailEmpresa').send_keys(email)
    sleep(1)
    driver.find_element(By.ID,'telefoneEmpresa').send_keys(telefone)
    sleep(1)
    driver.find_element(By.ID,'enderecoEmpresa').send_keys(endereco)
    sleep(1)
    driver.find_element(By.ID,'cnpj').send_keys(cnpj)
    sleep(1)
    driver.find_element(By.ID,'areaAtuacao').send_keys(area_atuacao)
    sleep(1)
    driver.find_element(By.ID,'numeroFuncionarios').send_keys(quantidade_de_funcionarios)
    sleep(1)
    driver.find_element(By.ID,'dataFundacao').send_keys(data_fundacao)
    sleep(1)

    # 7 – Clicar em cadastrar
    driver.find_element(By.ID,'Cadastrar').click()
    sleep(3)

    
