#!/usr/bin/python
# *-* encoding:utf-8 *-*

from bottle import run, route, default_app, get, post, request, template, static_file

import os
import re
import json
import requests
import urllib2




puertos = {1:'A coru&ntilde;a',3:'Vigo',4:'Vilagarc&iacute;a',5:'Ferrol',6:'R&iacute;a de 	Foz',7:'Corcubi&oacute;n',8:'R&iacute;a de Camari&ntilde;as',9:'R&iacute;a de Corme',10:'A guarda',11:'Ribeira',12:'Muros',13:'Pontevedra'}

clave = 'tntmnZ85PrQ6AGw6ihuUGhqs894jl66UI8p4ph4rmbvcno3MIApKE0o2N1awzT2p'


@route('../static/<filename>')
def server_static(filename):
  	return static_file(filename, root='../static/images/')

@route('../static/<filename>')
def server_static(filename):
  	return static_file(filename, root='../static/css/')


@route('/')
def index():
	return template('index1.html')

        
@post('/resultado')
def resultado():
		
	localidad = request.forms.get('localidad')
	url = 'http://servizos.meteogalicia.es/apiv3/findPlaces'	
	valores = {'location':localidad,'API_KEY':clave}
	req = requests.get(url, params=valores)
	response = json.loads(req.text)
	response['features'][0]['geometry']['coordinates']		
	longitud = str(response['features'][0]['geometry']['coordinates'][0])
	latitud = str(response['features'][0]['geometry']['coordinates'][1])	
	
	mareas = request.forms.get('mareas')
	url = 'http://servizos.meteogalicia.es/apiv3/getTidesInfo'
        valores = {'coord':mareas,'API_KEY':clave}
        req = requests.get(url, params=valores)
        response = json.loads(req.text)
	response['features'][0]['geometry']['coordinates']
                         
	pleamar = response['features'][0]['properties']['days'][0]['variables'][0]['summary'][0]['TimeInstant']   			 
        bajamar = response['features'][0]['properties']['days'][0]['variables'][0]['summary'][1]['TimeInstant']
        state_high = response['features'][0]['properties']['days'][0]['variables'][0]['summary'][0]['state']
        state_low = response['features'][0] ['properties']['days'][0]['variables'][0]['summary'][1]['state']
	
	semanal = request.forms.get('semanal')
	ident = request.forms.get('ident')
	return template('plantilla1.html', localidad=localidad, longi=longitud, lati=latitud, 
	plea=pleamar, baja=bajamar, state_high=state_high, state_low=state_low, id=ident, data=semanal)





	

# This must be added in order to do correct path lookups for the views
import os
from bottle import TEMPLATE_PATH
TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_HOMEDIR'], 
    'app-root/runtime/repo/wsgi/views/')) 

application=default_app()



