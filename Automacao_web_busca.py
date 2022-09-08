# criar um navegador
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd

nav = webdriver.Chrome()
tabela_produtos = pd.read_excel('buscas.xlsx')

def busca_google_shopping(nav,produto, termos_banidos, preco_minimo, preco_maximo):

    #entrar no google
    nav.get('https://www.google.com/')

    produto = produto.lower()
    termos_banidos = termos_banidos.lower()
    lista_termos_banidos = termos_banidos.split(" ")
    lista_termos_produto = produto.split(" ")


    #pesquisar o nome do produto no google
    nav.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(produto)
    nav.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

    #clicar na aba shopping
    elementos = nav.find_elements(By.CLASS_NAME, 'hdtb-mitem')
    for item in elementos:
        if "Shopping" in item.text:
            item.click()
            break

    #pegar lista de resultados no google shopping
    lista_resultados = nav.find_elements(By.CLASS_NAME, 'sh-dgr__content')

    #para cada resultado, verificar se o resultado corresponde a condiçoes
    lista_ofertas = []
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
            preco = resultado.find_element(By.CLASS_NAME, 'a8Pemb').text
            preco = preco.replace("R$", "").replace(" ", "").replace(".", "").replace(",", ".")
            preco = float(preco)

            preco_maximo = float(preco_maximo)
            preco_minimo = float(preco_minimo)
            if preco_minimo <= preco <= preco_maximo:
                elemento_link = resultado.find_element(By.CLASS_NAME, 'EI11Pd')
                elemento_pai = elemento_link.find_element(By.XPATH, '..')
                link = elemento_pai.get_attribute('href')
                lista_ofertas.append((nome, preco, link))


    return lista_ofertas

produto = 'iphone 12 64 gb'
termos_banidos = 'mini watch'
preco_minimo = 3000
preco_maximo = 8000

lista_ofertas_google_shopping = busca_google_shopping(nav, produto, termos_banidos, preco_minimo, preco_maximo)
print(lista_ofertas_google_shopping)

