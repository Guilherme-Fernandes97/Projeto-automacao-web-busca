# criar um navegador
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd

nav = webdriver.Chrome()
tabela_produtos = pd.read_excel('buscas.xlsx')


def busca_google_shopping(nav, produto, termos_banidos, preco_minimo, preco_maximo):
    # entrar no google
    nav.get("https://www.google.com/")

    # tratar os valores que vieram da tabela
    produto = produto.lower()
    termos_banidos = termos_banidos.lower()
    lista_termos_banidos = termos_banidos.split(" ")
    lista_termos_produto = produto.split(" ")
    preco_maximo = float(preco_maximo)
    preco_minimo = float(preco_minimo)

    # pesquisar o nome do produto no google
    nav.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(produto)
    nav.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(
        Keys.ENTER)

    # clicar na aba shopping
    elementos = nav.find_elements(By.CLASS_NAME, 'hdtb-mitem')
    for item in elementos:
        if "Shopping" in item.text:
            item.click()
            break

    # pegar a lista de resultados da busca no google shopping
    lista_resultados = nav.find_elements(By.CLASS_NAME, 'i0X6df')

    # para cada resultado, ele vai verificar se o resultado corresponde a todas as nossas condicoes
    lista_ofertas = []  # lista que a função vai me dar como resposta
    for resultado in lista_resultados:
        nome = resultado.find_element(By.CLASS_NAME, 'Xjkr3b').text
        nome = nome.lower()

        # verificacao do nome - se no nome tem algum termo banido
        tem_termos_banidos = False
        for palavra in lista_termos_banidos:
            if palavra in nome:
                tem_termos_banidos = True

        # verificar se no nome tem todos os termos do nome do produto
        tem_todos_termos_produto = True
        for palavra in lista_termos_produto:
            if palavra not in nome:
                tem_todos_termos_produto = False

        if not tem_termos_banidos and tem_todos_termos_produto:  # verificando o nome
            try:
                preco = resultado.find_element(By.CLASS_NAME, 'a8Pemb').text
                preco = preco.replace("R$", "").replace(" ", "").replace(".", "").replace(",", ".")
                preco = float(preco)
                # verificando se o preco ta dentro do minimo e maximo
                if preco_minimo <= preco <= preco_maximo:
                    elemento_link = resultado.find_element(By.CLASS_NAME, 'aULzUe')
                    elemento_pai = elemento_link.find_element(By.XPATH, '..')
                    link = elemento_pai.get_attribute('href')
                    lista_ofertas.append((nome, preco, link))
            except:
                continue

    return lista_ofertas

def busca_buscape(nav, produto, termos_banidos, preco_minimo, preco_maximo):
    # entrar no google
    nav.get("https://www.buscape.com.br/")

    # tratar os valores que vieram da tabela
    produto = produto.lower()
    termos_banidos = termos_banidos.lower()
    lista_termos_banidos = termos_banidos.split(" ")
    lista_termos_produto = produto.split(" ")
    preco_maximo = float(preco_maximo)
    preco_minimo = float(preco_minimo)

    # pesquisar o nome do produto no google
    nav.find_element(By.XPATH, '//*[@id="new-header"]/div[1]/div/div/div[3]/div/div/div[2]/div/div[1]/input').send_keys(produto, Keys.ENTER)


    # pegar a lista de resultados da busca no google shopping
    time.sleep(5)
    lista_resultados = nav.find_elements(By.CLASS_NAME, 'Cell_Content__fT5st')

    lista_ofertas = []
    for resultado in lista_resultados:
        try:
            preco = resultado.find_element(By.CLASS_NAME, 'CellPrice_MainValue__JXsj_').text
            nome = resultado.get_attribute('title')
            nome = nome.lower()
            link = resultado.get_attribute('href')

            tem_termos_banidos = False
            for palavra in lista_termos_banidos:
                if palavra in nome:
                    tem_termos_banidos = True

            tem_todos_termos_produto = True
            for palavra in lista_termos_produto:
                if palavra not in nome:
                    tem_todos_termos_produto = False

            if not tem_termos_banidos and tem_todos_termos_produto:
                preco = preco.replace("R$", "").replace(" ", "").replace(".", "").replace(",", ".")
                preco = float(preco)
                if preco_minimo <= preco <= preco_maximo:
                    lista_ofertas.append((nome, preco, link))

        except:
            pass
    return lista_ofertas


produto = 'iphone 12 64 gb'
termos_banidos = 'mini watch'
preco_minimo = 3500
preco_maximo = 4500

lista_ofertas_buscape = busca_buscape(nav, produto, termos_banidos, preco_minimo, preco_maximo)
print(lista_ofertas_buscape)

