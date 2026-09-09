Ejercicio 1.19: Antes del análisis, los datos transformados se cargan en un almacén de datos (Data Warehouse). Existen diferentes tipos de métodos de carga de datos. Se debe proporcionar el detalle de cada método de carga de datos utilizado en un proceso ETL.

Solución
En un proceso ETL (Extract, Transform, Load), después de extraer y transformar los datos, estos deben cargarse en un destino, como un Data Warehouse.

Los principales métodos de carga de datos utilizados en ETL son:

1. Carga completa (Full Load)
La carga completa consiste en cargar todos los datos disponibles desde el origen hacia el destino.

En cada ejecución, normalmente se reemplaza o reconstruye la información existente en el destino.

Características:

Se cargan todos los registros.
Es sencilla de implementar.
Puede requerir mucho tiempo y recursos cuando existe una gran cantidad de datos.
Es útil para la carga inicial de un Data Warehouse.
Ventajas:

Implementación sencilla.
Garantiza que todos los datos sean cargados.
Facilita la sincronización inicial.
Desventajas:

Consume más tiempo.
Requiere mayor procesamiento.
Puede generar una carga considerable sobre las fuentes y el Data Warehouse.
Ejemplo:

Si una tabla contiene 10 millones de registros, una carga completa vuelve a procesar y cargar los 10 millones de registros.

2. Carga incremental (Incremental Load)
La carga incremental solamente carga los datos nuevos o modificados desde la última ejecución del proceso ETL.

En lugar de procesar toda la información, se identifican los cambios y únicamente estos se cargan al Data Warehouse.

Características:

Procesa solamente los datos que han cambiado.
Es más rápida que una carga completa.
Requiere algún mecanismo para identificar los cambios.
Ventajas:

Reduce el tiempo de procesamiento.
Utiliza menos recursos.
Es adecuada para grandes volúmenes de datos.
Permite realizar cargas periódicas de manera eficiente.
Desventajas:

Es más compleja de implementar.
Se necesita identificar correctamente los registros nuevos o modificados.
Un error en el control de cambios puede provocar que algunos datos no se carguen.
Ejemplo:

Si una tabla contiene 10 millones de registros, pero solamente 5,000 fueron modificados desde la última ejecución, una carga incremental procesa únicamente esos 5,000 registros.

3. Carga por lotes (Batch Load)
La carga por lotes consiste en recopilar datos durante un determinado período y cargarlos al destino en un solo proceso.

La carga puede ejecutarse, por ejemplo:

Cada hora.
Cada día.
Cada semana.
Cada mes.
Características:

Los datos se acumulan antes de ser cargados.
Se ejecuta en horarios programados.
Es común en procesos ETL tradicionales.
Ventajas:

Permite procesar grandes cantidades de datos de manera organizada.
Reduce la cantidad de ejecuciones individuales.
Puede programarse para ejecutarse fuera del horario de mayor actividad.
Desventajas:

Los datos no están disponibles inmediatamente.
Puede generar una carga considerable durante la ejecución del lote.
Ejemplo:

Una empresa puede recopilar todas las ventas realizadas durante el día y cargarlas al Data Warehouse cada noche.

4. Carga en tiempo real (Real-Time Load)
La carga en tiempo real permite que los datos sean cargados al destino prácticamente inmediatamente después de generarse o modificarse en el sistema de origen.

Este método se utiliza cuando se necesita información actualizada continuamente.

Características:

Los datos se procesan continuamente.
Existe muy poca demora entre el origen y el destino.
Requiere tecnologías y sistemas capaces de procesar eventos o flujos de datos.
Ventajas:

Información prácticamente actualizada.
Permite tomar decisiones rápidamente.
Es útil para sistemas que requieren respuestas inmediatas.
Desventajas:

Mayor complejidad.
Requiere infraestructura especializada.
Puede ser más costoso de implementar y mantener.
Ejemplo:

Un sistema bancario puede enviar continuamente las transacciones realizadas hacia una plataforma de análisis para detectar operaciones sospechosas.

5. Carga por captura de cambios (Change Data Capture - CDC)
Change Data Capture (CDC) es una técnica que identifica los cambios realizados en los datos de origen, como:

Inserciones.
Actualizaciones.
Eliminaciones.
Estos cambios se envían posteriormente al Data Warehouse o sistema destino.

Características:

Detecta únicamente los cambios.
Puede utilizarse para cargas incrementales.
Reduce la necesidad de leer toda la tabla de origen.
Ventajas:

Muy eficiente para grandes volúmenes de datos.
Reduce el procesamiento inne
