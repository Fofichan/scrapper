from bs4 import BeautifulSoup
import requests
from tabulate import tabulate
import sqlite3

#create ouroborostore table
conn = sqlite3.connect('db.sqlite3')

base = 'https://www.wargaming.cl/collection/juegos-de-mesa?order=price&way=ASC&limit=24&page='


for page_number in range(1,2):
    url = base + str(page_number)
    response = requests.get(url)
    htmlContent = response.text
    soup = BeautifulSoup(htmlContent, 'html.parser')
    
    tituloElement = soup.findAll("h3", class_="bs-collection__product-title")
    precioOfertaElement = soup.findAll("del", class_="bs-collection__old-price")
    precioOfertaElement2 = soup.findAll("div", class_="bs-collection__product-final-price")
    linkElement = soup.findAll("a", class_="bs-collection__product-info", href=True)
    #print size of tituloElement
    print(len(tituloElement))
    print(len(precioOfertaElement))
    if len(tituloElement) == len(precioOfertaElement):
        for i in range(len(tituloElement)):
            titulo = tituloElement[i].text.strip()
            precio = precioOfertaElement[i].text.strip()
            precioOferta = precioOfertaElement2[i].text.strip()
            #get href value from linkElement
            enlace = 'https://www.wargaming.cl' + linkElement[i]['href']
            print(enlace)
            #print data
            #print("appending: " + titulo + " " + enlace)
        