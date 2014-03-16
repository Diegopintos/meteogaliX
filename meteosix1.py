#!/usr/bin/python
# *-* coding: UTF-8 *-*
import requests
import json

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



key = open('key.txt','r')
clave = ""
for lineas in key:
	clave = clave + lineas
clave = clave.replace("\n","")

provincia = int(raw_input("de que puerto quieres saber la informacion de las mareas\n"))
puertos = {1:'-8.4103,43.3635',3:'-8.7413,42.2237',4:'-8.76377,42.59795',5:'-8.23145,43.48696',6:'-7.25585,43.57058'
,7:'-9.19177,42.94544',8:'-9.18085,43.133',9:'-8.96078,43.26658',10:'-8.86991,41.90467',11:'-8.9918,42.5593',12:'-9.05726,42.77677',13:'-8.642,42.43318'}


url = 'http://servizos.meteogalicia.es/apiv2/getTidesInfo'
valores = {'coord':puertos[provincia],'format':'application/json','API_KEY':clave}
response = requests.get(url, params=valores)
dato = json.loads(response.text)
pleamar = dato['features'][0]['properties']['days'][0]['variables'][0]['summary'][0]['TimeInstant'] 
bajamar = dato['features'][0]['properties']['days'][0]['variables'][0]['summary'][1]['TimeInstant']
state_high_tides = dato['features'][0]['properties']['days'][0]['variables'][0]['summary'][0]['state']
state_low_tides = dato['features'][0]['properties']['days'][0]['variables'][0]['summary'][1]['state']
print "estado de la marea:",state_high_tides
print "la pleamar tuvo o tendrá lugar el dia y hora:",pleamar
print "estado de la marea:",state_low_tides
print "la bajamar tuvo o tendrá lugar el dia y hora",bajamar

