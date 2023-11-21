#Importamos las dependecias necesarias para el preprocesamiento
#pip install unidecode
#pip install -U spacy
from unidecode import unidecode
import spacy
import pandas as pd
import re

#Cargamos el archivo generado por la carga de datos
archivo_limpieza = '/content/Mlds6_Proyecto_Aplicado/docs/data/dfinal.xlsx'
df = pd.read_excel(archivo_limpieza)

#Usaremos Spacy para preprocesar todos nuestros testimonios
spacy.cli.download("es_core_news_sm")
nlp = spacy.load("es_core_news_sm")

#Separamos nuestros textos de las demas columnas
textos= df["Hecho Victimizante"]
textos

#Generamos el patrón para eliminar los espacios dobles
spaces = re.compile(r"\s{2,}")

#Generamos una fucnión en la cual se elimina palabras censuradas como los nombres y las cedulas de las victimas
def eliminar_palabras(patrones, texto):
    for patron in patrones:
        texto = re.sub(patron, '', texto)
    return texto

patrones = [r'\([^)]*\)',r'\b[Cc]\.[Cc]\. \w+\b|\b[Cc][Cc] \w+\b']

#Eliminamos nuestras palabras censuradas
textos_procesados = textos.apply(lambda x: eliminar_palabras(patrones, x))


#En esta función se genera el preprocesamiento de nuestro codigo
def preprocess(text):

    #Para cada texto generamos un objeto doc con nlp
    doc = nlp(text)

    #Filtramos los tokens que son stop_words
    filtered_tokens = filter(
        lambda token: not token.is_stop,
        doc
    )

    # Filtramos los tokens con longitud menor o igual a 1
    filtered_tokens2 = filter(
            lambda token: len(token) > 1,
            filtered_tokens
        )

    #Obtenemos los lemas de nuestros tokens
    lemmas = map(
            lambda token: token.lemma_,
            filtered_tokens2
            )
    lemma_text = " ".join(lemmas)

    #Los normalizamos luego de unirlos
    norm_text = unidecode(lemma_text)

    #Los pasamos a minusculas
    lower_text = norm_text.lower()

    #Finalmente unimos los tokens
    #Y limpiamos los espacios dobles y finales
    spaces_text = re.sub(spaces, " ", lower_text)
    return spaces_text.strip()

#Aplicamos la función a nuestro corpus
prep_corpus = textos_procesados.apply(preprocess)

#Generamos un archivo donde se guarda nuestro corpus preprocesado
prep_corpus.to_excel("/content/Mlds6_Proyecto_Aplicado/docs/data/prep_corpus.xlsx", index=False, header=True)
