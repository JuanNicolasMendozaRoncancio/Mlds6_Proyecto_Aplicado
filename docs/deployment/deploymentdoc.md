# Despliegue de modelos

## Infraestructura

- **Nombre del modelo:** Como ya se ha mencionado, el modelo es un modelo LDA, por lo que se le asignará el nombre "lda".
- **Plataforma de despliegue:** La plataforma en la que se desplegará el modelo es MLflow, utilizando una API para nuestro modelo. Se podrá acceder a ella mediante las bibliotecas adecuadas, como requests.
- **Requisitos técnicos:** Los requisitos para el despliegue y el buen funcionamiento de nuestro modelo son los siguientes:
  - Unidecode: Version 1.3.7
  - Spacy: Version 3.7.2
  - mlflow: Version 2.1.0 requests
  - pyngrok: Version 7.0.2
- **Requisitos de seguridad:** Para el despliegue del modelo, es necesario identificarse con su token de MLflow en la variable 'token' del código de despliegue.

## Código de despliegue

- **Archivo principal:** El documento que contiene el código de despliegue es el archivo main.py, ubicado en la carpeta deployment dentro de la carpeta scripts.
- **Rutas de acceso a los archivos:** No hay archivos necesarios para el despliegue de la API desde MLflow; todos los archivos necesarios se importan en el mismo código.
- **Variables de entorno:** Solo se requiere una variable para el despliegue:
   - token: Su propio token para conectarse con MLflow.

## Documentación del despliegue

- **Instrucciones de instalación:** La instalación del modelo debe realizarse en MLflow. Por lo tanto, es necesario conectarse con un servidor de la plataforma para subir el modelo. Por esta razón, debe ejecutar el código del archivo de despliegue en su propia máquina o PC después de haber ejecutado todos los archivos previos del 

- **Instrucciones de configuración:** La API no puede modificarse; lo único que podría ser modificable son el nombre del modelo y sus propios parámetros en la misma ejecución de MLflow.

- **Instrucciones de uso:** Dado que nuestro modelo es un modelo de temas, esta API se puede utilizar para identificar los temas a los que podría pertenecer un testimonio nuevo para el modelo. Esto se puede hacer con la biblioteca requests de Python.

- **Instrucciones de mantenimiento:** La API puede requerir mantenimiento, especialmente en su modelo adyacente, ya que fue entrenado con solo 940 testimonios, lo cual limita su confiabilidad.
