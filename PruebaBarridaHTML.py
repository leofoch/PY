from bs4 import BeautifulSoup
from urllib.request import urlopen
import mechanize
import os

# Instanciamos el objeto br
br = mechanize.Browser()

# Opciones para el navegador
# Ingnora robots.txt
br.set_handle_robots(False)
br.set_handle_equiv(False)
# Simula ser una persona
br.addheaders = [('User-agent', 'Mozilla/5.0')] 

# Opcion para terminar el bucle
opcion = "N"

# Pagina web
url = 'https://prenotami.esteri.it/'

br.open(url)   

br.select_form(nr= 0)

br.form[ 'Email' ] = "leofochtman@gmail.com"

br.form[ 'Password' ] = "Manzana1"
print(br.form[ 'Password' ])

 # Guardo el contenido del resultado de apretar el boton buscar en formato (html)
data = br.submit()
print(data)

#Estoy adentro y voy a la seccion servicios
#URL a recorrer
#URL a recorrer
url="https://prenotami.esteri.it/Services"

html = urlopen(url).read()
soup = BeautifulSoup(html,"lxml")
#print(soup)

tabla = soup.find_all("table", {"id" : "dataTableServices"})
print(tabla)