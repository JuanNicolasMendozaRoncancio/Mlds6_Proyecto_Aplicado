# Reporte del Modelo Baseline

## Descripción del modelo

El primer modelo generado fue el modelo LDA, luego de haber hecho una busqueda de hiperparametros con GridSearch se entreno con los siguientes hiperparametros:

* Numero de topicos:
* Metodo de aprendizaje:
* Maximo de iteraciones:

En él se obtuvieron la siguiente metrica perplexity y las palabras calve asociadas a cada uno de los topicos del modelo:


- Perplexity:
- Palabras de cada uno de los topicos:

## Variables de entrada

Las variables de entrada son los documentos (testimonios) que preprocesamos en nuestra exteacción de los datos.

## Evaluación del modelo

### Métricas de evaluación

Las principales metricas de evaluacion fueron las siguientes:

Perplexytu:
La perplejidad es una métrica comúnmente utilizada en el modelado de temas que resulta de una prueba de probabilidad retenida. Es una medida de inconsistencia, por lo que se prefieren valores más bajos. La perplejidad se utiliza para predecir los temas de documentos 'nuevos' para el modelo, que no formaron parte del corpus de entrenamiento. La interpretación de la perplejidad en el modelado de temas es que mide qué tan bien el modelo predice los datos retenidos. [1]

Y la evaluación de las palabras clave de cada uno delos topicos por personal humano. En este se asginaton valores de 0,1 en cada combinación posibles topicos para identificar que tan separados parecian segun la persepcion humana. (el valor sera mas cercano a uno mientras mas se parezcan los topicos)


### Resultados de evaluación

Tabla que muestra los resultados de evaluación del modelo baseline, incluyendo las métricas de evaluación.

## Análisis de los resultados

Vemos que el modelo presenta un perplejidad bastante alta, lo cual puede indicar que se adapta debilmente a nuevas muestras, esto se corrobra con la matriz generada por la evaluacion humana, la cual muestra varios valores cercanos a uno. Este fenomeo se puede deber a la falta de datos que se tiene al final de preprocesameinto junto con posibles errores en la busqueda de hiperparametros

## Conclusiones

Se tiene un modelo base con metricas que pueden ser mejoradas con más datos y una exploración más a fondo, sin embargo, en una evaluacion posterior con la herramienta pyLDAvis puede llevar a una mejor visualizavion de los topicos y su separacioon

## Referencias

[1\]: https://bookdown.org/gaston_becerra/curso-intro-r/modelado-de-topicos.html
