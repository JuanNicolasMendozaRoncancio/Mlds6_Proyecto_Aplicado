#Importamos las librerias necesarias
#!pip install wordcloud
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer


#Preparamos nuestro corpus
dfcorpus = pd.read_excel("/content/Mlds6_Proyecto_Aplicado/docs/data/prep_corpus.xlsx")
corpus = dfcorpus['Hecho Victimizante'].tolist()

#Obtenemos su representación y el vocabulario de la misma
vect = (
    CountVectorizer(max_features=1000, max_df=0.7)
    .fit(corpus)
    )
X = vect.transform(corpus)
X_np = X.toarray()
vocab = vect.get_feature_names_out()

#Entrenamos el modelo seleccionado
lda = LatentDirichletAllocation(
    max_iter= 50,
    n_components= 5,
    learning_method= "online"
    ).fit(X_np)


print("Veamos los topicos relacionados con un testimonio, por ejemplo el 777") 
features_lda = lda.transform(X_np)
doc_id = 777
doc_features = features_lda[doc_id]
fig, ax = plt.subplots()
ax.bar(np.arange(doc_features.size), doc_features);
ax.set_xlabel("Tópico");
ax.set_ylabel("Valor");
ax.set_xticks(np.arange(doc_features.size));
fig.show()


print("Imprimimos una nube de palabras para cada uno de los topicos")
components = lda.components_
fig, axes = plt.subplots(1, 5, figsize=(15, 3))
cont = 0
for j in range(5):
    ax = axes[j]
    freqs = {
        term: abs(float(importance))
        for term, importance in zip(vocab, components[cont])
    }
    wc = WordCloud(background_color="white").generate_from_frequencies(freqs)
    ax.imshow(wc)
    ax.axis("off")
    ax.set_title(f"Tópico {cont}")
    cont += 1
fig.show()



print("Análisamos la importancia de nuestros topicos en el corpus")
topic_importances = features_lda.mean(axis=0)

fig, ax = plt.subplots()
ax.bar(np.arange(topic_importances.size), topic_importances)
ax.set_xticks(np.arange(topic_importances.size));
ax.set_xlabel("Tópico")
ax.set_ylabel("Importancia")
fig.show()
