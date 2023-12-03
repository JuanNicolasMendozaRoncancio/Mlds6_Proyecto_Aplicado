%%writefile main.py
from sklearn.decomposition import LatentDirichletAllocation
from IPython.display import display
from pyngrok import ngrok
import pandas as pd
import numpy as np
import mlflow
import joblib
import os

#Conectamos con mlflow
command = """
mlflow server \
        --backend-store-uri sqlite:///tracking.db \
        --default-artifact-root file:mlruns \
        -p 5000 &
"""
get_ipython().system_raw(command)

token = " " # Agregue el token dentro de las comillas
os.environ["NGROK_TOKEN"] = token


!ngrok authtoken $NGROK_TOKEN


print(ngrok.connect(5000, "http"))


mlflow.set_tracking_uri("http://localhost:5000")

exp_id = mlflow.create_experiment(name="Testimonios", artifact_location="mlruns/")



dfBoW = pd.read_excel("/content/Mlds6_Proyecto_Aplicado/docs/data/BoWrepre.xlsx")
X_np = dfBoW.to_numpy()

#Entrenamos el modelo elegido
lda = LatentDirichletAllocation(
    max_iter=50,
    n_components=5,
    learning_method="online"
)
lda.fit(X_np)

#Lo guardamos con joblib
joblib.dump(lda, "lda_model.joblib")

#Subimos nuestro modelo a mlflow por medio de una run
with mlflow.start_run(run_name="lda", experiment_id=exp_id):
    # Log de hiperparámetros
    mlflow.log_params({
        "max_iter": 50,
        "n_components": 5,
        "learning_method": "online"
    })
    # Cargamos la metrica perplexity
    perplexity = lda.perplexity(X_np)
    mlflow.log_metric("perplexity", perplexity)

    # Log del modelo Gensim (como un artefacto)
    mlflow.log_artifact("lda_model.joblib")

#Creamos la API de mlflow
os.environ["MLFLOW_TRACKING_URI"] = "http://localhost:5000"

command = """
mlflow models serve -m 'models:/airline_delay/Production' -p 8001 --env-manager 'local' &
"""
get_ipython().system_raw(command)
