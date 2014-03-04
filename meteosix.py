#!/usr/bin/python
# *-* coding: UTF-8 *-*
import requests
from lxml import etree
import webbrowser

print """
1 A Coruña
3 Vigo
4 Villagarcía
5 Ferrol
6 Ría de Foz
7 Corcubión
8 Ría de Camarinas
9 Ría de Corme
10 A Guarda
11 Ribeira
12 Muros
13 Pontevedra
"""

file = open('salida.html','w')
provincia = int(raw_input("de que puerto, quieres saber la información de las mareas?:\n"))
puertos = {1:'A coruña',3:'Vigo',4:'Villagarcía',5:'Ferrol',6:'Ría de Foz'
,7:'Corcubión',8:'Ría de Camariñas',9:'Ría de Corme',10:'A guarda',11:'Ribeira',12:'Muros',13:'Pontevedra'}
api = raw_input("introduce tu api key:\n")
url = 'http://servizos.meteogalicia.es/apiv2/getTidesInfo'
valores = {'coord':'-8.637,43.45','format':'kml','API_KEY':api}
response = requests.get(url, params=valores)
dato = etree.fromstring(response.text.encode('utf-8'))
salida = etree.tostring(dato)
for element in salida.iter(tag='state'):
print element.tag

file.write(salida)



















	





	
	
		

	
	
	
	
