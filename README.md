# Proyecto Urban Grocers 

## Descripción
Este proyecto consiste en interactuar con la API de Urban Grocers para gestionar usuarios y kits. Se utiliza Python y la biblioteca `requests` para realizar las solicitudes HTTP.

## Requisitos
- Python 3.x
- Bibliotecas: `requests`
- pytest Si necesitas instalar `pytest`, puedes hacerlo desde la terminal de pycharm y en Python Packges buscar pytest

También es recomendable tener todas las dependencias necesarias en un archivo requirements.txt, que puedes usar para instalarlas:

bash

pip install -r requirements.txt


## Estructura de Archivos

El proyecto contiene los siguientes archivos:

- configuration.py: Contiene la configuración de la URL y las rutas de solicitud.
- data.py: Almacena los cuerpos de las solicitudes POST.
- sender_stand_request.py: Contiene funciones para enviar solicitudes a la API.
- create_kit_name_kit_test.py: Contiene las pruebas para crear kits.
- README.md: Este archivo de instrucciones.
- .gitignore: Archivos y carpetas que deben ser ignorados por Git.

## Documentación de la API
Abre la documentación para estudiar la API de la aplicación de Urban Grocers: <the URL of the launched server>/docs/.

## Endpoints Probados
- POST /kits: Creación de un nuevo kit de alimentos.
- GET /kits/{id}: Obtención de detalles de un kit específico.

## Lista de Comprobación de Pruebas automatizadas

#	Descripción	
- 1	El número permitido de caracteres (1): kit_body = { "name": "a" }	Código de respuesta: 201, El campo "name" coincide con el cuerpo de la solicitud.
- 2	El número permitido de caracteres (511): kit_body = { "name": "..." }	Código de respuesta: 201, El campo "name" coincide con el cuerpo de la solicitud.
- 3	El número de caracteres es menor que la cantidad permitida (0): kit_body = { "name": "" }	Código de respuesta: 400
- 4	El número de caracteres es mayor que la cantidad permitida (512): kit_body = { "name": "..." }	Código de respuesta: 400
- 5	Se permiten caracteres especiales: kit_body = { "name": "№%@," }	Código de respuesta: 201, El campo "name" coincide con el cuerpo de la solicitud.
- 6	Se permiten espacios: kit_body = { "name": " A Aaa " }	Código de respuesta: 201, El campo "name" coincide con el cuerpo de la solicitud.
- 7	Se permiten números: kit_body = { "name": "123" }	Código de respuesta: 201, El campo "name" coincide con el cuerpo de la solicitud.
- 8	El parámetro no se pasa en la solicitud: kit_body = { }	Código de respuesta: 400
- 9	Se ha pasado un tipo de parámetro diferente (número): kit_body = { "name": 123 }	Código de respuesta: 400

## ¿Cómo Ejecutar las Pruebas?
•  Clonar el repositorio en Pycharm: 
git clone git clone git@github.com:username/qa-project-Urban-Grocers-app-es.git
Navegar al directorio del proyecto: cd urban-grocers-api-testing
Instalar las dependencias: pip install -r requirements.txt
Ejecutar las pruebas: pytest

## Contribuciones

Si deseas contribuir a este proyecto, por favor sigue las pautas de contribución.
