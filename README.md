==========

#meteogaliX 
##aplicacion web sobre la informacion meteorologica y oceanografica en las costas de galicia

**meteogaliX** es una aplicacion web gratuita de uso libre que funciona conectandose a traves de la api de meteogalicia a traves de su URL: http://servizos.meteogalicia.es/apiv2
usa los metodos GET y POST de HTTP para poder consultar la informacion, y la devuelve en formato XML y JSON.
y se la presenta al usuario en formato amigable HTML.

**Funcionamiento de la aplicacion**

* se le solicitara al usuario que consulte la informacion de la busqueda de un dato, a traves de un formulario en HTML.

* se conectara con la api de meteogalicia que devolvera la informacion en formato JSON o XML.

* se leeran los datos, y se mostraran en formato HTML al usuario

* uno vez los datos sean mostrados, se usara la api de google maps para geolocalizar el lugar y mostrarlo en el mapa.

para entender mejor el uso de la api que se usara para la aplicacion, usamos los siguientes metodos proporcionados por la api de meteogalicia:

##metodos de uso de la api de meteogalicia

la api de meteogalicia, cuenta con los siguientes metodos, que le permiten al usuario consultar diferente informacion a traves de sus operaciones.

### operaciones usadas por la api de meteogalicia:

* ####**getTidesInfo**:
este metodo devuelve la informacion sobre las mareas
mas info: http://servizos.meteogalicia.es/api_manual/es/get_tides_info.html

* ####**getSolarInfo**:
este metodo muestra la informacion sobre salida y puesta del sol
mas info: http://servizos.meteogalicia.es/api_manual/es/get_solar_info.html#ref-get-solar-info

* ####**getNumericForecastInfo**
este metodo muestra la prediccion numerica, atmosferica y oceanografica
mas info: http://servizos.meteogalicia.es/api_manual/es/get_numeric_forecast_info.html#ref-get-numeric-forecast-info

* ####**findPlaces**
este metodo permite la busqueda de lugares a traves de una cadena de caracteres
mas info: http://servizos.meteogalicia.es/api_manual/es/find_places.html#ref-find-places

en el siguiente enlace, se muestra una tabla, de los parametros usados en las operaciones: 

http://servizos.meteogalicia.es/api_manual/es/operations.html#parametros-comunes-a-las-operaciones-getnumericforecastinfo-gettidesinfo-getsolarinfo

**algunos ejemplos de uso**

Obtener datos de mareas para el puerto más cercano a un punto concreto:

http://servizos.meteogalicia.es/apiv2/getTidesInfo?coord=-8.637,43.45&API_KEY=***

 


























