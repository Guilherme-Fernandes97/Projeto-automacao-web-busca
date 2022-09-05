# criar um navegador
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd

nav = webdriver.Chrome()

#importar/visualizar a base de dados
tabela_produtos = pd.read_excel('buscas.xlsx')
print(tabela_produtos)


#entrar no google
nav.get('https://www.google.com/')
produto = 'iphone 12 64gb'

#pesquisar o nome do produto no google
nav.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(produto)
nav.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
#clicar na aba shopping
nav.find_element(By.XPATH, '//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click()
#pegar o preço do produto no shopping



#para cada item dentro da base de dados
    #procurar esse produto no google shopping
        #verificar se algum dos produtos esta dentro da minha faixa de preço
    #procurar esse produro no buscape
        #verificar se algum dos produtos esta dentro da minha faixa de preço

#salvar as ofertas boas em uma dataframe
#exportar pro excel
#enviar por e-mail o resultado da tabela