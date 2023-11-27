# Reporte del Modelo Final

## Resumen Ejecutivo

El modelo final será el modelo base. Finalmente, se realizaron dos modelos, uno de LDA y otro de LSA, obteniendo las siguientes métricas de perplexity para el primero y evaluación humana para cada uno:

Modelo LSA:
* Tópico 0: esposo, pasar, ir, san, vicente, el, carro, decir, llegar, poder, florencia, caguan, momento, presidente, conductor,
* Tópico 1: abusar, sexual, abuso, embarazado, hecho, relato, desplazamiento, tortura, denuncia, año, encapuchado, violencia, edad, secuestro, santander,
* Tópico 2: año, alias, padre, frente, finca, secuestro, familia, hijo, vereda, municipio, senor, secuestrar, millon, el, hecho,
* Tópico 3: llegar, llevar, ir, decir, casa, tener, dejar, carro, matar, el, yo, vereda, comandante, persona, llamar,
* Tópico 4: municipio, grupo, frente, policia, guerrillero, año, secuestro, militar, encontrar, secuestrar, corregimiento, ep, vehiculo, armado, hora,

Modelo LDA:
* Tópico 0: esposo, pasar, ir, san, vicente, el, carro, decir, llegar, poder, florencia, caguan, momento, presidente, conductor,
* Tópico 1: abusar, sexual, abuso, embarazado, hecho, relato, desplazamiento, tortura, denuncia, año, encapuchado, violencia, edad, secuestro, santander,
* Tópico 2: año, alias, padre, frente, finca, secuestro, familia, hijo, vereda, municipio, senor, secuestrar, millon, el, hecho,
* Tópico 3: llegar, llevar, ir, decir, casa, tener, dejar, carro, matar, el, yo, vereda, comandante, persona, llamar,
* Tópico 4: municipio, grupo, frente, policia, guerrillero, año, secuestro, militar, encontrar, secuestrar, corregimiento, ep, vehiculo, armado, hora,

* Perplexity: 526.7825654984

Se observa que las métricas del modelo base, aunque la diferencia no es significativa, son mejores que las del modelo LSA, por lo cual se elige el primero.

## Descripción del Problema

El objetivo inicial era la identificación de tópicos en un corpus formado por testimonios enmarcados en el conflicto armado colombiano. Este conflicto ha causado un gran daño en nuestro país, y es por esto que debemos utilizar todas nuestras herramientas para abordarlo y comprenderlo de la mejor manera. Es por esto que se utiliza el modelo de tópicos para identificar tópicos relevantes en un conjunto medianamente grande de testimonios.

El modelo presentado cumple con este objetivo, ya que presenta 5 tópicos medianamente diferentes con los cuales se podría abordar cada una de las problemáticas representadas en los tópicos individuales.

## Descripción del Modelo

El modelo final es un modelo de análisis de tópicos usando LDA con las siguientes métricas:

* Número de tópicos: 5
* Método de aprendizaje: online
* Máximo de iteraciones: 50

Para construir este modelo, se implementó una metodología CRISP-DM que se puede ver ilustrada en este mismo repositorio. Además, para la búsqueda de hiperparámetros se hizo una búsqueda en grilla con GridSearchCV.

## Evaluación del Modelo

Las métricas trabajadas para este modelo son la métrica perplexity y la evaluación humana ya descrita anteriormente.

* Perplexity: 526.7825654984

| Topicos | Topico 0 | Topico 1 | Topico 2 | Topico 3 | Topico 4 |

| Topico 0 | 1 | 0.7 | 0.5 | 0.2 | 0.4 |

| Topico 1 | 0.7 | 1 | 0.2 | 0.2 | 0.5 |

| Topico 2 | 0.5 | 0.2 | 1 | 0.7 | 0.5 |

| Topico 3 | 0.4 | 0.5 | 0.7 | 1 | 0.2 |

| Topico 4 | 0.4 | T0.5 | 0.5 | 0.2 | 1 |


Se observa entonces que nuestro modelo podría tener cierta dificultad al adaptarse a nuevos datos, esto debido a que la cantidad de testimonios era bastante baja, lo cual da pie a que el modelo no sea tan robusto. También, en la matriz de evaluación humana se observa que los tópicos no son tan distintos.


Sin embargo podemos ver junto con las palbaras clave la siguinte posible distinción de topicos:

- Topico 0: Un topico general.
- Topico 1: Crimenes relacionados con el abuso sexual
- Topico 2: Crimenes relacionados con el secuestro
- Topico 3: Posiblemente crimenes relacionados con la extorción
- Topico 4: Posiblemente crimenes relacionados con atentados

## Conclusiones y Recomendaciones

Se concluye entonces que, para tener un modelo más robusto y realmente aplicable, se deben considerar más parámetros y realizar una búsqueda de hiperparámetros más exhaustiva. Esto se debe a que con pocos testimonios, los tópicos suelen no estar lo suficientemente separados para distinguirlos. Sin embargo, el modelo es un primer paso hacia un modelo más complejo pero a su vez más amplio, con el cual se podrían enfocar investigaciones que aborden a lo largo del conflicto armado y su historia en nuestro país.
