from bs4 import BeautifulSoup
import requests
from tabulate import tabulate
import sqlite3

#create ouroborostore table
conn = sqlite3.connect('db.sqlite3')

#enlace base
base = 'https://www.ouroborostore.cl/categoria-producto/juegos-de-mesa/page/'
#itera por  página
for page_number in range(1,999):
    #solicita y carga contenido de página
    url = base + str(page_number) + '/'
    response = requests.get(url)
    htmlContent = response.text
    soup = BeautifulSoup(htmlContent, 'html.parser')
    
    #busca título, precio y enlace
    tituloElement = soup.findAll("p", class_="name product-title")
    priceElement = soup.findAll("span", class_="price")
    linkElement = soup.findAll("a", class_="")

    if len(tituloElement) == len(priceElement):
        data = []
        for i in range(len(tituloElement)):
            #extrae título, precio normal, precio oferta y enlace
            titulo = tituloElement[i].text.strip()
            precio_completo = priceElement[i].text.strip()
            precios = precio_completo.split(" ")
            precio_normal = precios[0]
            precio_oferta = precios[1] if len(precios) > 1 else None
            enlace = tituloElement[i].find('a').get('href')
            #añade a la lista
            data.append([titulo, precio_normal, precio_oferta, enlace])
            print("appending: " + titulo)
            #inserta en db
            c = conn.cursor()
            c.execute("INSERT INTO ouroborostore (titulo, precio_normal, precio_oferta, enlace) VALUES (?, ?, ?, ?)", (titulo, precio_normal, precio_oferta, enlace))
            conn.commit()
    else:
        print("Error: las listas de títuloss y precios no tienen la misma longitud")
        