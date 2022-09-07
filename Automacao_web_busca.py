# criar um navegador
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd

nav = webdriver.Chrome()

#importar/visualizar a base de dados
tabela_produtos = pd.read_excel('buscas.xlsx')


#entrar no google
nav.get('https://www.google.com/')

produto = 'iphone 12 64 gb'
termos_banidos = 'mini watch'

produto = produto.lower()
termos_banidos = termos_banidos.lower()
lista_termos_banidos = termos_banidos.split(" ")
lista_termos_produto = produto.split(" ")
preco_minimo = 3000
preco_maximo = 3500

#pesquisar o nome do produto no google
nav.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(produto)
nav.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

#clicar na aba shopping
elementos = nav.find_elements(By.CLASS_NAME, 'hdtb-mitem')
for item in elementos:
    if "Shopping" in item.text:
        item.click()
        break

lista_resultados = nav.find_elements(By.CLASS_NAME, 'i0X6df')

for resultado in lista_resultados:

    nome = resultado.find_element(By.CLASS_NAME, 'Xjkr3b').text
    nome = nome.lower()

    #verificação de nome
    tem_termos_banidos = False
    for palavra in lista_termos_banidos:
        if palavra in nome:
            tem_termos_banidos = True

    tem_todos_termos_produtos = True
    for palavra in lista_termos_produto:
        if palavra not in nome:
            tem_todos_termos_produtos = False

    if not tem_termos_banidos and tem_todos_termos_produtos:
        preco = resultado.find_element(By.CLASS_NAME, 'kHxwFf').text
        preco = preco.replace("R$", "").replace(" ", "").replace(".", "").replace(",", ".")
        preco = str(preco[:5])
        preco = float(preco)

        preco_maximo = float(preco_maximo)
        preco_minimo = float(preco_minimo)
        if preco_minimo <= preco <= preco_maximo:
            elemento_link = resultado.find_element(By.CLASS_NAME, 'EI11Pd')
            elemento_pai = elemento_link.find_element(By.XPATH, '..')
            link = elemento_pai.get_attribute('href')
            print(nome, preco, link)







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