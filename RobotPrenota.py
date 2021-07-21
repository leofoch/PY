from bs4 import BeautifulSoup
from urllib.request import urlopen





pagina="""
<div id="dataTableServices_wrapper" class="dataTables_wrapper no-footer"><div class="dt-buttons"></div><table id="dataTableServices" class="display dataTable no-footer" role="grid" style="width: 1168px;"><thead><tr role="row"><th class="sorting" tabindex="0" aria-controls="dataTableServices" rowspan="1" colspan="1" aria-label="Categor&amp;#237;a: activate to sort column ascending" style="width: 127px;">Categoría</th><th class="sorting" tabindex="0" aria-controls="dataTableServices" rowspan="1" colspan="1" aria-label="Servicio : activate to sort column ascending" style="width: 224px;">Servicio </th><th class="sorting" tabindex="0" aria-controls="dataTableServices" rowspan="1" colspan="1" aria-label="Descripci&amp;#243;n: activate to sort column ascending" style="width: 228px;">Descripción</th><th class="sorting_disabled" rowspan="1" colspan="1" aria-label="Reserva " style="width: 176px;">Reserva </th><th class="sorting_disabled" rowspan="1" colspan="1" aria-label="Enlace" style="width: 125px;">Enlace</th><th class="sorting_disabled" rowspan="1" colspan="1" aria-label="correo electr&amp;#243;nico" style="width: 72px;">correo electrónico</th></tr></thead><tbody><tr role="row" class="odd"><td>DOCUMENTOS DE IDENTIDAD Y DE VIAJE</td><td>Pasaporte</td><td> Entrega de pasaportes</td><td><a href="/Services/Booking/223"><button class="button primary" style="width:7.00rem;">Reservar </button></a></td><td><p><a href="https://consbuenosaires.esteri.it/consolato_buenosaires/es/i_servizi/per-i-cittadini/approfondimento-passaporto.html#RITIRO" target="_blank"><i class="fa fa-external-link-alt"></i>&nbsp;&nbsp;Enlace&nbsp;1</a></p></td><td></td></tr><tr role="row" class="even"><td>SERVICIOS CONSULARES</td><td>Servicios Consulares</td><td>Notarial</td><td><a href="/Services/Booking/225"><button class="button primary" style="width:7.00rem;">Reservar </button></a></td><td><p><a href="https://consbuenosaires.esteri.it/consolato_buenosaires/it/i_servizi/per-i-cittadini/notarile2012-05-18.html" target="_blank"><i class="fa fa-external-link-alt"></i>&nbsp;&nbsp;Enlace&nbsp;1</a></p></td><td></td></tr><tr role="row" class="odd"><td>SERVICIOS CONSULARES</td><td>Servicios Consulares</td><td>Estudios</td><td><a href="/Services/Booking/227"><button class="button primary" style="width:7.00rem;">Reservar </button></a></td><td><p><a href="https://consbuenosaires.esteri.it/consolato_buenosaires/it/i_servizi/per-i-cittadini/studi2012-05-27.html" target="_blank"><i class="fa fa-external-link-alt"></i>&nbsp;&nbsp;Enlace&nbsp;1</a></p></td><td></td></tr><tr role="row" class="even"><td>REGISTRO DE LA POBLACIÓN Y ESTADO CIVIL</td><td>Estado Civil</td><td>Vice Consulado Honorario en San Isidro</td><td><a href="/Services/Booking/228"><button class="button primary" style="width:7.00rem;">Reservar </button></a></td><td><p><a href="https://consbuenosaires.esteri.it/consolato_buenosaires/es/i_servizi/per-i-cittadini/adozioni.html" target="_blank"><i class="fa fa-external-link-alt"></i>&nbsp;&nbsp;Enlace&nbsp;1</a></p></td><td></td></tr><tr role="row" class="odd"><td>REGISTRO DE LA POBLACIÓN Y ESTADO CIVIL</td><td>Estado Civil</td><td>Corresponsal Consular en Tres de Febrero</td><td>Calendario de reservas no disponible aún.</td><td><p><a href="https://consbuenosaires.esteri.it/consolato_buenosaires/it/i_servizi/per-i-cittadini/adozioni.html" target="_blank"><i class="fa fa-external-link-alt"></i>&nbsp;&nbsp;Enlace&nbsp;1</a></p></td><td></td></tr><tr role="row" class="even"><td>REGISTRO DE LA POBLACIÓN Y ESTADO CIVIL</td><td>Estado Civil</td><td>Corresponsal Consular en Zarate</td><td><a href="/Services/Booking/230"><button class="button primary" style="width:7.00rem;">Reservar </button></a></td><td><p><a href="https://consbuenosaires.esteri.it/consolato_buenosaires/es/i_servizi/per-i-cittadini/adozioni.html" target="_blank"><i class="fa fa-external-link-alt"></i>&nbsp;&nbsp;Enlace&nbsp;1</a></p></td><td></td></tr><tr role="row" class="odd"><td>REGISTRO DE LA POBLACIÓN Y ESTADO CIVIL</td><td>Estado Civil</td><td>Corresponsal Consular en Merlo</td><td><a href="/Services/Booking/231"><button class="button primary" style="width:7.00rem;">Reservar </button></a></td><td><p><a href="https://consbuenosaires.esteri.it/consolato_buenosaires/it/i_servizi/per-i-cittadini/adozioni.html" target="_blank"><i class="fa fa-external-link-alt"></i>&nbsp;&nbsp;Enlace&nbsp;1</a></p></td><td></td></tr><tr role="row" class="even"><td>SERVICIOS CONSULARES</td><td>Servicios Consulares</td><td>Legalizaciones para Naturalización</td><td><a href="/Services/Booking/233"><button class="button primary" style="width:7.00rem;">Reservar </button></a></td><td><p><a href="https://consbuenosaires.esteri.it/consolato_buenosaires/es/i_servizi/per-i-cittadini/natumatr.html" target="_blank"><i class="fa fa-external-link-alt"></i>&nbsp;&nbsp;Enlace&nbsp;1</a></p></td><td></td></tr><tr role="row" class="odd"><td>SERVICIOS CONSULARES</td><td>Servicios Consulares</td><td>Certificación de traducciones actas del Registro Civil</td><td>Calendario de reservas no disponible aún.</td><td><p><a href="https://consbuenosaires.esteri.it/consolato_buenosaires/it/i_servizi/per-i-cittadini/notarile2012-05-18.html#conformita" target="_blank"><i class="fa fa-external-link-alt"></i>&nbsp;&nbsp;Enlace&nbsp;1</a></p></td><td></td></tr><tr role="row" class="even"><td>SERVICIOS CONSULARES</td><td>Servicios Consulares</td><td>Oficina de Pensiones - Certificado Supervivencia</td><td>Calendario de reservas no disponible aún.</td><td><p><a href="https://consbuenosaires.esteri.it/consolato_buenosaires/es/i_servizi/per-i-cittadini/pensioni2012-05-20.html" target="_blank"><i class="fa fa-external-link-alt"></i>&nbsp;&nbsp;Enlace&nbsp;1</a></p></td><td></td></tr></tbody></table><div class="dataTables_paginate paging_simple_numbers" id="dataTableServices_paginate"><a class="paginate_button previous disabled" aria-controls="dataTableServices" data-dt-idx="0" tabindex="0" id="dataTableServices_previous">Previous</a><span><a class="paginate_button current" aria-controls="dataTableServices" data-dt-idx="1" tabindex="0">1</a><a class="paginate_button " aria-controls="dataTableServices" data-dt-idx="2" tabindex="0">2</a></span><a class="paginate_button next" aria-controls="dataTableServices" data-dt-idx="3" tabindex="0" id="dataTableServices_next">Next</a></div></div>
"""


#URL a recorrer
url="https://prenotami.esteri.it/Services"

html = urlopen(url).read()
soup = BeautifulSoup(html,"lxml")
tables = soup.findAll("table")

#header del navegador (me hago pasar por un navegador)
#header = {"User-Agent":"Mozilla/5.0 Gecko/20100101 Firefox/33.0 GoogleChrome/10.0"}

#Obtengo la pagina
#page = requests.get(url, headers=header)

#r = requests.get(url)
#soup = BeautifulSoup(r.text, 'lxml')
#soup = BeautifulSoup(pagina, 'lxml')

#Parseo el contenido
#soup = BeautifulSoup(page.content,'lxml')
#soup = BeautifulSoup(pagina,'lxml')
print(soup.title)
tds=[]
#tabla = soup.find_all('div')
#tabla = soup.find_all(class_='main-nav__flag')
tabla = soup.find_all(id='main')
#print(tabla)
for row in tabla:
#tds.append(rows.findAll('td'))
#print(str(tds))
	if row.text.find("Accedi")>0:
		print (row.text)


#ListaJobs = soup.find_all(id='dataTableServices_wrapper')
#print(ListaJobs)

#print(soup.div.div)
#pp= soup.find("td", text="Passaporto").find_next_sibling("td").text
#print(pp)
