import pandas as pd
import numpy as np
from sklearn.decomposition import TruncatedSVD
from sklearn.model_selection import GridSearchCV
from sklearn.metrics.pairwise import cosine_similarity

param_grid = {
    'n_components': [5, 10, 15, 20],  # Número de tópicos
    'n_iter': [10, 50, 100],  # Número máximo de iteraciones
}
lsa = TruncatedSVD()
grid_search = GridSearchCV(lsa, param_grid=param_grid, cv=5, verbose=2, scoring='v_measure_score')


dfTFIDF = pd.read_excel("/content/Mlds6_Proyecto_Aplicado/docs/data/TFIDFrepre.xlsx")
X_np = dfTFIDF.to_numpy()


grid_search.fit(X_np)

best_lsa = grid_search.best_estimator_
components = best_lsa.components_

lsa = TruncatedSVD(
    n_iter= grid_search.best_params_["n_iter"],
    n_components=grid_search.best_params_["n_components"],
    ).fit(X_np)

vocabu = pd.read_excel("/content/Mlds6_Proyecto_Aplicado/docs/data/VocabTFIDF.xlsx")
vocab = vocabu.to_numpy()


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
    # Mostramos los términos más importantes en cada tópico
    print(
            "Tópico {}: {}".format(
                i,
                " ".join(list(map(lambda x: str(x[0]), sorted_terms)))
                )
            )
