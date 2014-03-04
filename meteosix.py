#!/usr/bin/python
#*-* coding: UTF-8 *-*
import requests
from jinja2 import Template
import json
from lxml import etree


entrada = raw_input("introduce tu api key:\t")
url = 'http://servizos.meteogalicia.es/apiv2/getTidesInfo' 
valores = {'coord':'-8.637,43.45','API_KEY':'%s'}
valores['API_KEY'] = entrada
response = requests.get(url, params=valores)
dato = json.loads(response.text.encode('UTF-8'))
lista_puertos = []
lista.puertos.append(dato)

	





	
	
		

	
	
	
	
