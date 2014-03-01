#!/usr/bin/python
#*-* coding: UTF-8 *-*
import requests
from jinja2 import Template
import json
from lxml import etree

dicc = {'API_KEY':'tntmnZ85PrQ6AGw6ihuUGhqs894jl66UI8p4ph4rmbvcno3MIApKE0o2N1awzT2p'}
response = requests.get('http://servizos.meteogalicia.es/apiv2/getTidesInfo', params={'coord':'-8.637,43.45','format':'application/json','API_KEY'
:'tntmnZ85PrQ6AGw6ihuUGhqs894jl66UI8p4ph4rmbvcno3MIApKE0o2N1awzT2p'})
dato = json.loads(response.text)
list_datos = []
list_datos.append(dato)
for i in list_datos:
	coordenadas = i['features'][0]['geometry']['coordinates']
	for e in coordenadas:
		print e

	
	
	
	
