#!/usr/bin/python
# -*- coding: utf-8 -*-
from bottle import route, run, get, post, template, request
import json
import requests

@route('/index')
def index():
    return ''' <html>
		<head>
		<title></title>
		<body>
		<div>
		<h1>Formulario de busqueda por localidades</h1>
		<form method="POST" action="/index">
		<select name="localidad"/>
		<option value="a coruña">a coruña</option>
		<option value="vigo">Vigo</option>
		<option value="Vilagarcia">Vilagarcía</option>
		<option value="Ferrol">Ferrol</option>
		<option value="Foz">Ría de Foz</option>
		<option value="corcubión">Corcubión</option>
		<option value="camariñas">Ría de Camariñas</option>
		<option value="corme">Ría de Corme</option>
		<option value="a guarda">A guarda</option>
		<option value="ribeira">Ribeira</option>
		<option value="Muros">Muros</option>
		<option value="Pontevedra">Pontevedra</option>
		</select>
		<input type="submit" value="enviar">
		</form>
		<h1>Busqueda por coordenadas</h1>
		<h5>introduce una coordenada, por longitud y latitud</h5>
		<form action="/mareas"method="POST">
		<label><b>coordenada</b></label><input type="text"name="mareas">
		<input type="submit"value="enviar">
		</form>
		</div>
		</body>
		</html>'''



@post('/mareas')
def getTidesInfo():
	mareas = request.forms.get('mareas')
	API='tntmnZ85PrQ6AGw6ihuUGhqs894jl66UI8p4ph4rmbvcno3MIApKE0o2N1awzT2p'
	req = requests.get('http://servizos.meteogalicia.es/apiv2/getTidesInfo', params={'coord':mareas,'format':'text/html','API_KEY':API})
        response = json.loads(req.text)
	pleamar = response['features'][0]['properties']['days'][0]['variables'][0]['summary'][0]['TimeInstant']
        req1 = requests.get('http://servizos.meteogalicia.es/apiv2/getTidesInfo', params={'coord':mareas,'format':'text/html','API_KEY':API})
	response1 = json.loads(req1.text)
	bajamar = response['features'][0]['properties']['days'][0]['variables'][0]['summary'][1]['TimeInstant']
	return template('<p>la bajamar tuvo lugar el dia: {{bajamar}}</p><p>la pleamar tuvo lugar el dia:{{pleamar}}', bajamar=bajamar, pleamar=pleamar)
	
	
		
@post('/index')
def findPlaces():
        localidad = request.forms.get('localidad')
	API='tntmnZ85PrQ6AGw6ihuUGhqs894jl66UI8p4ph4rmbvcno3MIApKE0o2N1awzT2p'
        req = requests.get('http://servizos.meteogalicia.es/apiv2/findPlaces', params={'location':localidad,'API_KEY':API})
        response = json.loads(req.text)
        return response
	
	 
						


run(host='localhost', port=8080, debug=True)
