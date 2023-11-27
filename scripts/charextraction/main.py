#Justificación de las representaciones:
print("""
Como realizaremos un modelado de tópicos, usaremos uno de los dos modelos más utilizados: LSA o LDA. Veamos cuáles son las ventajas de cada uno en nuestro caso:

LSA:
A pesar de tener un bajo costo computacional, no posee una buena interpretación final ya que nos proporciona un número en lugar de una probabilidad, lo cual es una desventaja en nuestro caso.
Sin embargo, este modelo sera usado para tener un punto de comparación con los demas posibles modelos.

LDA:
El LDA es común en el análisis de tópicos y tiene una alta interpretabilidad, aunque tiene un costo computacional mayor que el LSA.

Con respecto al embedding que usaremos, LSA usa TF-IDF y LDA usa BoW. Estas dos representaciones son aplicables a nuestro corpus, que contiene pocos datos (ya que tenemos menos de 10,000 documentos.)

Finalmente, como compararemos los modelos LSA y LDA. Usaremos ambas representaciones, tanto TF-IDF como BoW.
""")

#Importamos todas las librerias necesarias
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

#Extraemos nuestro corpus
dfprep = pd.read_excel("/content/Mlds6_Proyecto_Aplicado/docs/data/prep_corpus.xlsx")
corpus = dfprep["Hecho Victimizante"].to_list()

#Extracción de caracteristicas usando BoW
vect = (CountVectorizer(max_features=1000, max_df=0.7).fit(corpus))
X = vect.transform(corpus)
X_np = X.toarray()
vocab = vect.get_feature_names_out()
#Guardamos nuestra representación como un archivo xlsx
dfBoW = pd.DataFrame(X_np)
dfBoW.to_excel("/content/Mlds6_Proyecto_Aplicado/docs/data/BoWrepre.xlsx", index=False)




#Extracción de caracteristicas usando TF-IDF
tfidf_vectorizer = TfidfVectorizer(max_features=1000, max_df=0.7)
X_tfidf = tfidf_vectorizer.fit_transform(corpus)
X_tfidf_np = X_tfidf.toarray()
vocabu = tfidf_vectorizer.get_feature_names_out()
#Guardamos nuestra representación como xlsx
dfTFIDF = pd.DataFrame(X_tfidf_np)
dfTFIDF.to_excel("/content/Mlds6_Proyecto_Aplicado/docs/data/TFIDFrepre.xlsx", index=False)
