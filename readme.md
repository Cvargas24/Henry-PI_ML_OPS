## Proyecto Individual - Data Engineer 


> En este README encontrarán toda la documentación, e instrucciones necesarias, para poder utilizar la API y el Sistema de Recomendación que se  solicitó desarrollar.

[Video explicativo](https://www.youtube.com/watch?v=D02HngLv77A)

**MENU:** 
* **Data** - _carpeta con los dataset de las 4 plataformas._
* **Machine Learning** - _carpeta que contiene la parte de EDA y el Sistema de Recomendación. ._
* **limpieza.ipynb** - _notebook con las transformaciones pedidas._
* **main.py** - _contiene el llamado de la APi._
* **README** - _Instrucciones de uso._
* ** queries.py** - _contiene las funciones de las queries pedidas._
* **spark.py** - _contiene el calculo de la columnas soore._ 
* **requirements.txt** - _dependencias necesarias para que funcione._

**Las funciones que componen la API son:**

-  Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN. (la función debe llamarse get_max_duration(año, plataforma, duración_tipo)). <br>
-  Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año. <br>
-  Cantidad de películas por plataforma con filtro de PLATAFORMA. (La función debe llamarse get_count_platform(plataforma)). <br>
- Actor que más se repite según plataforma y año. (La función debe llamarse get_actor(platform, year)) <br>


** Enlace para descargar la API**

https://deta.space/discovery/r/ipy5pbozxzzaqj6h

** Cómo escribir cada función en el navegador**

- https://space_p01-2-f2485253.deta.app/get_word_count/{platform}/{anio}/{duration_type}
- https://space_p01-2-f2485253.deta.app/get_score_count/{platform}/{scored}/{anio}
- https://space_p01-2-f2485253.deta.app/get_count_platform/{platform}
- https://space_p01-2-f2485253.deta.app/get_actor/{platform}/{anio}

**Queries de ejemplo para probar la API**

- https://space_p01-2-f2485253.deta.app/get_word_count/amazon/2010/min
- https://space_p01-2-f2485253.deta.app/get_score_count/amazon/3.6/2012
- https://space_p01-2-f2485253.deta.app/get_count_platform/netflix
- https://space_p01-2-f2485253.deta.app/get_actor/disney/2015



**Machine Learning**


Ya los datos están limpios, investigamos las relaciones que hay entre las variables de los datasets, ver si hay outliers o anomalías , y ver si hay algún patrón interesante que valga la pena explorar en un análisis posterior, para ello realizamos un Análisis Exploratorio de Datos-EDA.

Por terminar desarrollamos nuestro Sistema de Recomendación. En este caso nos basamos en el algoritmo de SVD


