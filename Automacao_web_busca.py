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
elementos = nav.find_elements(By.CLASS_NAME, 'hdtb-mitem')
for item in elementos:
    if "Shopping" in item.text:
        item.click()
        break

lista_resultados = nav.find_elements(By.CLASS_NAME, 'KZmu8e')

for resultado in lista_resultados:
    preco = resultado.find_element(By.CLASS_NAME, 'T14wmb').text
    nome = resultado.find_element(By.CLASS_NAME, 'ljqwrc').text
    elemento_link = resultado.find_element(By.CLASS_NAME, 'HUOptb')
    elemento_pai = elemento_link.find_element(By.XPATH, '..')
    link = elemento_pai.get_attribute('href')
    print(preco, nome, link)




#for elemento_preco in lista_precos:

#pegar o preço do produto no shopping



#para cada item dentro da base de dados
    #procurar esse produto no google shopping
        #verificar se algum dos produtos esta dentro da minha faixa de preço
    #procurar esse produro no buscape
        #verificar se algum dos produtos esta dentro da minha faixa de preço

#salvar as ofertas boas em uma dataframe
#exportar pro excel
#enviar por e-mail o resultado da tabela