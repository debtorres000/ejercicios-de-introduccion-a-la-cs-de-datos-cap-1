Ejercicio 1.15 Los datos son recolectados de diferentes fuentes en formatos diversos. Debido a eso, es probable que la informacion recolectada este sucia. Para limpiarla, se usa el método de Extracción, Transformacion y Carga de datos (ETL). Proporciona los detalles de este método y explica cómo funciona. 

El proceso ETL se divide en tres fases.  

Extracción. 

 Siendo el primer paso, se encarga de recolectar y obtener la data de sus diferentes fuentes para almacenarlas temporalmente para los siguentes pasos en el proceso de ETL. Existen tres diferentes tipos:  

1.1 Extraccion completa. 

1.2 Extraccion parcial sin notificacion de actualización. 

1.3 Extracción parcial con notificación de actualización. 

 

Transformación 

 Este es el paso central del proceso de ETL, se puede comparar con un filtro o 	revision de los datos extraídos en el paso anterior antes de consumar el proceso 	BI. Este proceso dependerá de la estructura y estado de los datos extraídos por 	lo que éste variará dependiendo de las necesidades de la empresa u 	organización. 

Ya que su objetivo principal es homogenizar la información para el paso final de 	este proceso los retos mas comunes vienen de errores de digitación / grabado 	de datos, variacion en la semantica de un mismo termino o concepto y omisión 	de información. 

Existen dos tipos de transformación:  

2.1 Transformacion por etapas. Requiere extraer los datos para transformarlos de manera remota en un almacen inmediato y luego éstos son movida para su almacenamiento. 

2.2  Transfromacion dentro del alamacén. Este proceso no requiere de un almacenamiento inmediato despues de recuperarlo de la fuente, sino que los datos se mueven directamente hacia el almacén y ahí son procesados. 

 

Carga 

Este es el último paso del proceso, donde los datos son cargados al almacén. Por la naturaleza de este proceso, la carga muchas veces es fallida o dañada durante los intentos de carga ya que se considera una enorme cantidad de datos, por lo anterior, es importante contar con un respaldo de la información antes y durante este proceso para no perder el progreso de los datos obtenidos. 

Existen diferentes tipos: 

3.1 Carga completa: Todos los datos son cargados al almacen por primera vez. 

3.2 Carga por incremento: Es una carga seccionada para ser cargada por partes guardando checkpoints. 
