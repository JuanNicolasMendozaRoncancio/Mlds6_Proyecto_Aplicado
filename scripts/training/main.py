import pandas as pd
import numpy as np
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.model_selection import GridSearchCV
from sklearn.metrics.pairwise import cosine_similarity

param_grid = {
    'n_components': [5,10,15,20],  # Número de tópicos
    'learning_method': ['batch', 'online'],  # Método de aprendizaje
    'max_iter': [10,50,100],  # Número máximo de iteraciones
}
lda = LatentDirichletAllocation()
grid_search = GridSearchCV(lda, param_grid=param_grid, cv=5, verbose=2)

dfBoW = pd.read_excel("/content/Mlds6_Proyecto_Aplicado/docs/data/BoWrepre.xlsx")
X_np = dfBoW.to_numpy()


grid_search.fit(X_np)

best_lda = grid_search.best_estimator_
components = best_lda.components_

lda = LatentDirichletAllocation(
    max_iter= grid_search.best_params_["max_iter"],
    n_components=grid_search.best_params_["n_components"],
    learning_method= grid_search.best_params_['learning_method']
    ).fit(X_np)

df = pd.read_excel("/content/Mlds6_Proyecto_Aplicado/docs/data/VocabBow.xlsx")
vocab = df.to_numpy()

# Iteramos sobre cada tópico
for i, comp in enumerate(components):
    # Juntamos los términos con cada uno de los valores en la matriz V
    terms_comp = zip(vocab, np.abs(comp))
    # Ordenamos los términos de acuerdo al resultado de LSA
    sorted_terms = sorted(
            terms_comp,
            key=lambda x: x[1],
            reverse=True
            )[:15]
    # Convertimos los términos a cadenas de texto antes de unirlos
    terms_str = list(map(lambda x: str(x[0]), sorted_terms))
    # Mostramos los términos más importantes en cada tópico
    print(
            "Tópico {}: {}".format(
                i,
                " ".join(terms_str)
                )
            )

perplexity = lda.perplexity(X_np)
print(f"Perplexity:{perplexity}")
