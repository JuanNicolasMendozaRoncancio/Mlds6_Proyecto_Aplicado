## Análisis de sentimientos en testimonios del conflicto armado colombiano

La historia de la guerra forma parte integral de la historia de nuestro país. No es casualidad que hayamos experimentado un conflicto armado, uno de los más violentos en la historia reciente del mundo, durante más de 70 años.

Las consecuencias de este conflicto se reflejan más en el ámbito social que en el económico. Después de todo, quienes luchan y sufren en la guerra no son los líderes políticos, sino la gente común. A continuación, se presentan varias cifras correspondientes a 4,698 eventos victimizantes. [1]:

* Desplazamiento: 12,190 (26 %)
* Amenazas: 8,457 (18 %)
* Homicidio: 6,956 (14.8 %)
* Tortura: 2,589 (5.5 %)
* Exilio: 2,379 (5.1 %)
* Desaparición: 1,961 (4.2 %)
* Despojo: 1,677 (3.6 %)
* Secuestro: 1,663 (3.5 %)
* Atentado: 1,545 (3.3 %)
* Violencia sexual: 1,294 (2.8 %)
* Reclutamiento: 1,136 (2.4 %)
* Ataque indiscriminado: 880 (1.9 %)
* Detención arbitraria: 835 (1.8 %)
* Extorsión: 824 (1.8 %)
* Confinamiento: 807 (1.7 %)
* Pillaje: 751 (1.6 %)
* Ataque a bien protegido: 611 (1.3 %)
* Trabajo forzoso: 383 (0.8 %)

Entre 1985 y 2018, se registraron en Colombia al menos 450,664 homicidios como resultado del conflicto armado interno. No obstante, al tener en cuenta el subregistro, esta cifra se estima en alrededor de 800,000 víctimas. Los paramilitares fueron los principales autores de estos asesinatos, responsables de aproximadamente el 45% de los casos, mientras que los grupos guerrilleros y los agentes estatales representaron el 27% y el 12%, respectivamente. [2]

En cuanto a los testimonios del conflicto armado, la JEP y la Comisión de la Verdad tienen la tarea de garantizar la veracidad de los mismos. En el informe final de la Comisión de la Verdad, se encuentran recopilados más de 27,000 testimonios tanto de víctimas como de victimarios. Estos testimonios se obtuvieron a lo largo de 14,000 entrevistas en Colombia y en otros 27 países.[3].

Algunas cifras destacadas de este informe son:

* El 80% de las víctimas fueron civiles no combatientes.
* Más de 110,000 desaparecidos.
* 30,000 niños menores de 15 años reclutados por grupos armados.
* 6,402 personas asesinadas en ejecuciones extrajudiciales del Ejército

## Objetivo del Proyecto

Como hemos visto, el conflicto armado deja atrás una cantidad considerable de testimonios que deben analizarse con cuidado y respeto. Es por esto que el objetivo de este proyecto es, mediante el uso de NLP y análisis de tópicos, llegar a un entendimiento más profundo de los testimonios a analizar. Se busca una caracterización de los temas que se pueden extraer e inferir de los testimonios dados.

## Alcance del Proyecto

- Descripción de los datos disponibles:

Usaremos datos de texto obtenidos de testimonios de víctimas del conflicto armado en Colombia. Los datos están disponibles en la sala de prensa de la JEP, específicamente en este [enlace](https://www.jep.gov.co/Sala-de-Prensa/Documents/CASO%2001%20TOMA%20DE%20REHENES/25..01.2021%20Anexo%20ADHC.pdf?csf=1&e=EXdU3t). Los testimonios se obtienen de víctimas de todo el territorio nacional, y se han censurado los nombres y cédulas de las personas para preservar su privacidad.

Se espera obtener un análisis de tópicos profundo que pueda visualizarse en representaciones como nubes de palabras para cada uno de los tópicos, junto con una posible visualización en pyLDAvis.

Se considerará exitoso el proyecto si logramos caracterizar los testimonios en uno o más tópicos. Además, el modelo utilizado en el proyecto debería ser extrapolable para un posible análisis de sentimientos.

### Excluye:

En el proyecto no se incluirá un análisis numérico de los datos, ya que no es necesario para nuestros objetivos.

## Metodología

La metodología a usar será una adaptación de la metodología TDSP a una sola persona, es decir, nuestra metodología será más cercana a CRISP-DM.

## Cronograma

| Etapa | Duración Estimada | Fechas |
|------|---------|-------|
| Entendimiento del negocio y carga de datos | 1 semana | del 13 de noviembre al 17 de noviembre |
| Preprocesamiento, análisis exploratorio | 1 semana | del 20 de noviembre al 24 |
| Modelamiento y extracción de características | 1 semana | del 27 de noviembre al 1 de diciembre |
| Despliegue | 1 semana | del 16 de julio al 31 de julio |
| Evaluación y entrega final | 1 semana | del 2 de diciembre al 8 de diciembre |


[1]:https://web.comisiondelaverdad.co/actualidad/noticias/principales-cifras-comision-de-la-verdad-informe-final
[2]:https://es.statista.com/grafico/19344/numero-de-victimas-del-conflicto-armado-en-colombia/
[3]:https://www.aa.com.tr/es/mundo/la-comisión-de-la-verdad-publica-el-informe-final-sobre-más-de-medio-siglo-de-conflicto-en-colombia/2625032
