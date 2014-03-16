#!/usr/bin/python
# *-* coding: UTF-8 *-*
import requests
import webbrowser
import json
from jinja2 import Template

 
print """
1 	A Coruña
3 	Vigo
4 	Villagarcía
5 	Ferrol
6 	Ría de Foz
7 	Corcubión
8 	Ría de Camarinas
9 	Ría de Corme
10	 A Guarda
11	 Ribeira
12	 Muros
13	 Pontevedra 
	"""

file = open('plantilla.html','r')
html = open('mareas.html','w')
key = open('key.txt','r')
clave = ""
for lineas in key:
	clave = clave + lineas
clave = clave.replace("\n","")

puertos = {1:'A coru&ntilde;a',3:'Vigo',4:'Vilagarc&iacute;a',5:'Ferrol',6:'R&iacute; de Foz',7:'Corcubi&oacute;n',8:'R&iacute;a de Camari&ntilde;as',9:'R&iacute; de Corme',10:'A guarda',11:'Ribeira',12:'Muros',13:'Pontevedra'}	

coordenada = {1:'-8.4103,43.3635',3:'-8.7413,42.2237',4:'-8.76377,42.59795',5:'-8.23145,43.48696',6:'-7.25585,43.57058'
,7:'-9.19177,42.94544',8:'-9.18085,43.133',9:'-8.96078,43.26658',10:'-8.86991,41.90467',11:'-8.9918,42.5593',12:'-9.05726,42.77677',13:'-8.642,42.43318'}

lista_puertos = ['A Coruña',
       'Vigo',
       'Villagarcía',
       'Ferrol',
       'Ría de Foz',
       'Corcubión',
       'Ría de Camarinas',
       'Ría de Corme',
       'A Guarda',
       'Ribeira',
       'Muros',
       'Pontevedra']


lista_pleamar = []
lista_bajamar = []
	
for n in coordenada.values():
	url = 'http://servizos.meteogalicia.es/apiv2/getTidesInfo'
	valores = {'coord':n,'format':'application/json','API_KEY':clave}
	response = requests.get(url, params=valores) 
print "estado de las mareas en las costas de galicia:\n"
print "los resultados se toman cada 30 minutos en los puertos mas cercanos\n"
for l in lista_puertos:
        
	dato = json.loads(response.text)
	print "puerto de:",l
	pleamar = dato['features'][0]['properties']['days'][0]['variables'][0]['summary'][0]['TimeInstant'] 
	bajamar = dato['features'][0]['properties']['days'][0]['variables'][0]['summary'][1]['TimeInstant']
	state_high_tides = dato['features'][0]['properties']['days'][0]['variables'][0]['summary'][0]['state']
	state_low_tides = dato['features'][0] ['properties']['days'][0]['variables'][0]['summary'][1]['state']
	print "la marea tiene un estado de:",state_high_tides
	print "la pleamar tuvo o tendrá lugar el dia y hora:",pleamar
	print "la marea tiene un estado de:",state_low_tides
	print "la bajamar tuvo o tendrá lugar el dia y hora",bajamar
	print "\n"
	lista_pleamar.append(pleamar)	
		
		
pagina = ""
for t in file:
 pagina += t
plantilla = Template(pagina)
salida = plantilla.render(puertos=puertos.values(), plea=lista_pleamar, baj=bajamar, state_ple=state_high_tides, state_ba=state_low_tides)	
html.write(salida)
webbrowser.open('mareas.html')
		
	
	
		
		
		

	
	
	
	
		
		

	
	
		
	




	


	
	





	





	
	
		

	
	
	
	
