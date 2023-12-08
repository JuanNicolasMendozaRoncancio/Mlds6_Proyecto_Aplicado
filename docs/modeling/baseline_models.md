# Reporte del Modelo Baseline

## Descripción del modelo

El primer modelo generado fue el modelo LDA. Después de realizar una búsqueda de hiperparámetros con GridSearch, se entrenó con los siguientes valores:

* Número de tópicos: 5
* Método de aprendizaje: online
* Máximo de iteraciones: 50

Se obtuvieron las siguientes métricas de perplexity y las palabras clave asociadas a cada uno de los tópicos del modelo:

* Perplexity: 526.7825654984
* Palabras de cada uno de los tópicos:
 * Tópico 0: esposo, pasar, ir, san, vicente, el, carro, decir, llegar, poder, florencia, caguan, momento, presidente, conductor,
 * Tópico 1: abusar, sexual, abuso, embarazado, hecho, relato, desplazamiento, tortura, denuncia, año, encapuchado, violencia, edad, secuestro, santander,
 * Tópico 2: año, alias, padre, frente, finca, secuestro, familia, hijo, vereda, municipio, senor, secuestrar, millon, el, hecho,
 * Tópico 3: llegar, llevar, ir, decir, casa, tener, dejar, carro, matar, el, yo, vereda, comandante, persona, llamar,
 * Tópico 4: municipio, grupo, frente, policia, guerrillero, año, secuestro, militar, encontrar, secuestrar, corregimiento, ep, vehiculo, armado, hora,

## Variables de entrada

Las variables de entrada son los documentos (testimonios) que preprocesamos durante la extracción de datos.

### Métricas de evaluación

Las principales métricas de evaluación fueron las siguientes:

Perplexity:
La perplejidad es una métrica comúnmente utilizada en el modelado de temas que resulta de una prueba de probabilidad retenida. Es una medida de inconsistencia, por lo que se prefieren valores más bajos. La perplejidad se utiliza para predecir los temas de documentos 'nuevos' para el modelo, que no formaron parte del corpus de entrenamiento. La interpretación de la perplejidad en el modelado de temas es que mide qué tan bien el modelo predice los datos retenidos. 1

La evaluación también incluyó la asignación de valores de 0 a 1 para cada combinación posible de tópicos, según la percepción humana, para identificar qué tan separados parecían los tópicos. (El valor será más cercano a uno mientras más se parezcan los tópicos)


### Resultados de evaluación

Tenemos las siguientes tablas que muestran la evalucaión de nuestro modelo:

* Perplexity: 526.7825654984

| Topicos | Topico 0 | Topico 1 | Topico 2 | Topico 3 | Topico 4 |
|------|---------|-------|-------|-------|-------|
| Topico 0 | 1 | 0.7 | 0.5 | 0.2 | 0.4 |
| Topico 1 | 0.7 | 1 | 0.2 | 0.2 | 0.5 |
| Topico 2 | 0.5 | 0.2 | 1 | 0.7 | 0.5 |
| Topico 3 | 0.4 | 0.5 | 0.7 | 1 | 0.2 |
| Topico 4 | 0.4 | T0.5 | 0.5 | 0.2 | 1 |

## Análisis de los resultados

Observamos que el modelo presenta una perplejidad bastante alta, lo cual puede indicar una adaptación débil a nuevas muestras. Esto se confirma con la matriz generada por la evaluación humana, la cual muestra varios valores cercanos a uno. Este fenómeno podría deberse a la falta de datos al final del preprocesamiento junto con posibles errores en la búsqueda de hiperparámetros.

## Conclusiones

Contamos con un modelo base cuyas métricas podrían mejorarse con más datos y una exploración más detallada. Sin embargo, una evaluación posterior con la herramienta pyLDAvis podría proporcionar una mejor visualización de los tópicos y su separación.

## Referencias

[1\]: https://bookdown.org/gaston_becerra/curso-intro-r/modelado-de-topicos.html
