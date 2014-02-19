
==========



#meteogalic 
##aplicacion web sobre la informacion meteorologica en las costas de galicia

**meteogalic** es una aplicacion web gratuita de uso libre que funciona conectandose a traves de la api de meteogalicia a traves de su URL: http://servizos.meteogalicia.es/apiv2
usa los metodos GET y POST de HTTP para poder consultar la informacion, y la devuelve en formato XML y JSON.
y se la presenta al usuario en formato amigable HTML.

##metodos de uso de la api de meteogalicia

la api de meteogalicia, cuenta con los siguientes metodos, que le permiten al usuario consultar diferente informacion a traves de sus operaciones.

### operaciones usadas por la api de meteogalicia:

* ####**getTidesInfo**:
este metodo devuelve la informacion sobre las mareas

* ####**getSolarInfo**:
este metodo muestra la informacion sobre salida y puesta del sol

* ####**getNumericForecastInfo**
este metodo muestra la prediccion numerica, atmosferica y oceanografica

* ####**findPlaces**
este metodo permite la busqueda de lugares a traves de una cadena de caracteres

los parametros utilizados para estas operaciones son los siguientes:

1. ####**API_KEY**

es un parametro obligatorio, por que la api de meteosix requiere autenticacion para su uso, a traves de una clave publica, que es unica para cada cuenta de correo. 

2. ####**locationId**
es el identificador que devuelve datos sobre un lugar, este parametro es opcional

3. ####**coord**
este parametro define las coordenadas, y devuelve datos sobre ellas, deben ser 2 y estar separadas por comas, en el caso de coordenadas geograficas, el orden es longitud y latitud
es un parametro opcional.

* valores posibles:
x,y donde x,y son coordenadas desde longitud y latitud

4. ####**startTime**
este parametro devuelve la informacion sobre el primer instante temporal, sino se indica, devuelve desde el primer instante disponible.
es un parametro opcional.

* valores posibles:
a;o:mes:dia:horas:minutos:segundos

5. ####**endTime**
este parametro devuelve la informacin sobre el ultimo instante temporal, sino se indica devuelve hasta el ultimo instante disponible, dentro de sus limites establecidos para cada peticion.
este parametro es opcional.

* valores posibles:
a;o:mes:dia:horas:minutos:segundos

6. ####**lang**
este parametro define en que idioma quieres en el que se devuelvan la informacion, incluyendo los textos para las excepciones.
este parametro es opcional.

* valores posibles: gl, es, en por defecto: "en"

7. ####**tz**
este parametro define la zona horaria en la que se mostrara la hora
* valores posibles: por defecto : "Europe/Madrid"

8. ####**CRS**
este parametro define el sistema de coordenadas


