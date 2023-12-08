# Informe de salida

## Resumen Ejecutivo

## Resultados del proyecto

- Se diseñó un modelo de análisis de tópicos utilizando testimonios enmarcados en el conflicto armado colombiano. En cada una de las etapas del proyecto se logró y entregó:
  - **Entendimiento del negocio y carga de datos:**
Se logró identificar el problema inicial y cargar los testimonios. Un informe más detallado se encuentra en: project_charter.md
  - **Preprocesamiento y análisis exploratorio de datos:**
Se llevó a cabo un análisis exploratorio, analizando nuestro corpus a nivel de palabra y de carácter, además de encontrar una relación entre estas variables. También logramos preprocesar nuestros datos de manera adecuada para nuestro modelo. Para más detalles, consulte data_summary.md, main.py de data_preprocessing y main.py en la carpeta eda.
  - **Modelado y extracción de características:**
Se extrajeron las características de nuestros datos usando dos métodos: BoW y TF-IDF, y posteriormente se entrenó un modelo para cada una de las representaciones: LDA y LSA. Esto se encuentra en la carpeta charextraction de scripts, en la carpeta training, main.py para LDA y LSA.py para LSA, y la totalidad de la carpeta modeling.
  - **Despliegue:**
Se generó una API con la ayuda de Mlflow la cual puede ser usada en la generación de clases para modelos predictivos, o en la creación de estrategias para abordar las problemáticas. Los documentos de esta fase se encuentran en el archivo main.py de la carpeta deployment y deploymentdoc de la carpeta deployment.
  - **Evaluación:**
Se evalúa el modelo con diferentes visualizaciones y ejemplos, entre ellas se encuentra la visualización de los diferentes tópicos en nuestro corpus.
- Evaluación del modelo final y comparación con el modelo base:
El modelo final es un modelo LDA con los siguientes parámetros:

  - Número de iteraciones: 50
  - Número de tópicos: 5
  - Método de aprendizaje: Online

El modelo base era el mismo modelo que se usó, ya que el modelo LSA no presentaba mejora en ambas métricas evaluadas

- Descripción de los resultados y su relevancia para el negocio.
Los siguientes fueron los tópicos encontrados por nuestro modelo:

  - Tópico 1: Tópico General
  - Tópico 2: Abuso Sexual
  - Tópico 3: Secuestro
  - Tópico 4: Extorsión
  - Tópico 5: Atentados
  
Para ver una nube de palabras de cada tópico puede ir a la carpeta imágenes. También podemos ver la distribución de tópicos en nuestro corpus en esta misma carpeta y la distribución de tópicos para un documento dado como lo es el 777.

Este modelo puede ser escalado usando más testimonios y más visualizaciones que no pudieron ser implementadas usando pyLDAvis para poder tener más tópicos o tópicos mejor definidos. Este proceso de refinamiento podría llevar a categorías más adecuadas y esto a su vez llevaría a estrategias más claras para afrontar las problemáticas asociadas a cada tópico.

## Lecciones aprendidas

- Identificación de los principales desafíos y obstáculos encontrados durante el proyecto:
En este proyecto se encontraron diversos desafíos, como la falta de datos, lo que implicó que nuestro modelo llegara a tener los tópicos no tan bien definidos. También se encontraron problemas en la implementación de pyLDavis, ya que generaba un conflicto con varias librerías.

- Lecciones aprendidas en relación al manejo de los datos, el modelado y la implementación del modelo:
Notamos que el manejo de textos implica el manejo de datos personales que deben ser tratados en el preprocesamiento de los datos. También, los textos deben ser entendidos bajo su propio contexto. El modelado se debe realizar con varios tipos de modelos para poder comparar y escoger el que mejor se adapte a nuestro objetivo. Es importante saber qué APIs se pueden crear con nuestro modelo y cuáles podemos crear en nuestro contexto. Finalmente, se deben verificar las dependencias necesarias para el uso de ciertas librerías, como pyLDAvis.

- Recomendaciones para futuros proyectos de machine learning.
Para futuros proyectos de ML, se recomienda usar una buena cantidad de datos. También, poder identificar qué APIs se ajustan mejor a nuestros objetivos y cuáles son realizables.


## Impacto del proyecto

- Descripción del impacto del modelo en el negocio o en la industria.
El modelo se puede usar para la identificación de tópicos en nuevos testimonios entrantes; a su vez, también se puede usar para identificar e implementar estrategias que aborden las problemáticas expuestas en cada tópico.
- Identificación de las áreas de mejora y oportunidades de desarrollo futuras.
Hay varias áreas de mejora:

  - No se tiene una cantidad adecuada de datos.
  - Se podría implementar un segundo modelo que clasifique textos entrantes en cada uno de los tópicos generados por nuestro modelo.
  - Generar APIs útiles con nuestros modelos de ML, en especial de modelos no predictivos.
  - Asegurarse de que todas las librerías sean compatibles.

## Conclusiones

- Resumen de los resultados y principales logros del proyecto.
Los principales resultados y logros del proyecto se componen en la realización del modelo como tal. Tener un modelo capaz de identificar los tópicos más comunes en un grupo dado de testimonios puede llegar a ser un paso significativo en la búsqueda de la verdad del conflicto armado en Colombia. Además de esto, el proceso que se usó para llegar al mismo modelo puede ser mejorado usando más datos o refinando el preprocesamiento de los mismos.

- Conclusiones finales y recomendaciones para futuros proyectos.
Tener un modelo de análisis de tópicos en el marco del conflicto armado puede ser de gran utilidad, especialmente si se tienen grandes cantidades de textos para el propio corpus. Sin embargo, se recomienda tener claro qué APIs generar y qué librerías usar para la evaluación de nuestro modelo.
