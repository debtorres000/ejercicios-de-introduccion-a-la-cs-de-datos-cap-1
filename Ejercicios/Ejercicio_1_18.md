Ejercicio 1.18: ¿Cuántos métodos de extracción de datos tenemos? Se requiere proporcionar los detalles de cada método.

Solución
Existen 4 métodos principales de extracción de datos:

1. Extracción manual
La extracción manual consiste en que una persona recopila los datos directamente de una fuente y los registra en otro sistema o archivo.

Características:

Requiere intervención humana.
Puede realizarse mediante formularios, hojas de cálculo o registros manuales.
Es sencilla de implementar.
Es adecuada cuando la cantidad de datos es pequeña.
Ventajas:

No requiere herramientas o software especializado.
Permite verificar los datos durante la recopilación.
Desventajas:

Es lenta cuando existe una gran cantidad de información.
Puede producir errores humanos.
Es difícil de escalar.
Ejemplo: copiar manualmente información de clientes desde documentos impresos hacia una hoja de Excel.

2. Extracción mediante archivos
En este método, los datos se obtienen desde archivos que contienen información estructurada o semiestructurada.

Algunos ejemplos de archivos son:

CSV
Excel (.xlsx)
XML
JSON
Archivos de texto
Características:

Permite procesar grandes cantidades de información.
Puede automatizarse mediante programas o scripts.
Los datos pueden ser estructurados o semiestructurados.
Ventajas:

Es relativamente sencilla de automatizar.
Permite procesar grandes volúmenes de información.
Es compatible con muchas herramientas de análisis.
Desventajas:

Los archivos pueden tener diferentes formatos.
Pueden existir problemas de calidad o consistencia de los datos.
Es necesario controlar las versiones y ubicaciones de los archivos.
Ejemplo: extraer información de ventas desde un archivo CSV para cargarla posteriormente en una base de datos.

3. Extracción desde bases de datos
Consiste en obtener información directamente desde una base de datos utilizando consultas, normalmente mediante SQL.

Entre las bases de datos que pueden utilizarse se encuentran:

MySQL
PostgreSQL
SQL Server
Oracle
SQLite
Características:

Permite consultar grandes cantidades de datos.
Utiliza consultas para seleccionar únicamente la información necesaria.
Puede realizarse de forma periódica y automatizada.
Ventajas:

Es eficiente para grandes volúmenes de datos.
Permite realizar filtros y transformaciones durante la extracción.
Facilita la automatización de procesos.
Desventajas:

Requiere conocimientos de bases de datos y SQL.
Se necesitan permisos adecuados para acceder a la información.
Las consultas complejas pueden consumir muchos recursos.
Ejemplo:

SELECT nombre, correo, fecha_registro
FROM clientes
WHERE fecha_registro >= '2026-01-01';

Esta consulta extrae los clientes registrados a partir del 1 de enero de 2026.

4. Extracción mediante APIs o servicios web
Las APIs (Application Programming Interfaces) permiten obtener datos de una aplicación o servicio externo de manera programática.

Los datos suelen proporcionarse en formatos como:

JSON
XML
Características:

Permite la comunicación entre diferentes aplicaciones.
Puede utilizarse para obtener datos en tiempo real o de manera periódica.
Normalmente requiere autenticación y autorización.
Ventajas:

Permite automatizar completamente la extracción.
Puede proporcionar información actualizada.
Facilita la integración entre diferentes sistemas.
Desventajas:

Puede requerir una clave o token de acceso.
Algunas APIs tienen límites de solicitudes.
Los cambios en la API pueden afectar el proceso de extracción.
Ejemplo: una aplicación puede utilizar una API para obtener información de productos, usuarios o transacciones de otro sistema.

Resumen
Método	Fuente de datos	Automatización	Ejemplo
Extracción manual	Documentos, formularios, registros	Baja	Copiar datos a Excel
Archivos	CSV, Excel, JSON, XML	Alta	Leer un archivo CSV
Bases de datos	MySQL, PostgreSQL, SQL Server, etc.	Alta	Consulta SQL
APIs / servicios web	Aplicaciones y servicios externos	Alta	Obtener datos mediante una API

Respuesta final
En este ejercicio se identifican 4 métodos principales de extracción de datos:

Extracción manual
Extracción mediante archivos
Extracción desde bases de datos
Extracción mediante APIs o servicios web
Cada método tiene diferentes características, ventajas y desventajas, y la elección depende principalmente de la fuente, el volumen de información y el nivel de automatización requerido.
