from bs4 import BeautifulSoup
import requests
from tabulate import tabulate

#request
url = "https://www.magicsur.cl/15-juegos-de-mesa-magicsur-chile?resultsPerPage=99999"
response = requests.get(url)
htmlContent = response.text
soup = BeautifulSoup(htmlContent, 'html.parser')
print(response.status_code)
#busca título, precio y enlace
tituloElement = soup.findAll("h2", class_="h3 product-title")
precioNormalElement = soup.findAll("span", class_="product-price")
precioOfertaElement = soup.findAll("span", class_="regular-price text-muted")
linkElement = soup.findAll("a", class_="")

print(len(tituloElement), len(precioNormalElement))
if len(tituloElement) == len(precioNormalElement):
    data = []
    for i in range(0, len(tituloElement)):
        #extrae título, precio normal, precio oferta y enlace
        titulo = tituloElement[i].text.strip()
        precioNormal = precioNormalElement[i].text.strip()
        precioOferta = precioOfertaElement[i].text.strip()
        enlace = tituloElement[i].find('a').get('href')
        #añade a la lista
        data.append([titulo, precioNormal, precioOferta, enlace])
        headers = ["Título", "Precio Normal", "Precio Oferta", "Enlace"]
        print(tabulate(data, headers=headers, tablefmt="grid"))
    else:
        print("Error: las listas de títulos y precios no tienen la misma longitud")
        