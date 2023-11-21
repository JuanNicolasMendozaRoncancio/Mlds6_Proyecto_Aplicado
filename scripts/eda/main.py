import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Resumen General de los datos
archivo = '/content/Mlds6_Proyecto_Aplicado/docs/data/dfinal.xlsx'
df = pd.read_excel(archivo)

tamby = os.path.getsize('/content/Mlds6_Proyecto_Aplicado/docs/data/dfinal.xlsx')
tammb = tamby / (1024 * 1024)

textos = df["Hecho Victimizante"]

print(f"Estamos trabajando con {len(textos)} testimonios")
print(f"El tamaño de nuestro archivo es {tammb:.2f} MB\n")


#Resumen de la caldidad de los datos
faltan = textos.isna().any()
if faltan:
  print("Faltan testimonios\n")
else:
  print("No hay testimonios flatantes\n\n")


#Análisis a nivel de palabra
palabras = df["Hecho Victimizante"]
palabras_sep = palabras.apply(lambda texto: texto.split())
palbrasLong = palabras_sep.apply(lambda lista: len(lista))
print("La siguiente es una tabla que muestra el indice del testimonio y el numero de palabras en el mismo:\n")
print(palbrasLong)
print("\n")

print("Pasemos a análisar con mayor profundidad la longuitud en palabras de nuestros testimonios:\n")
print(palbrasLong.describe())
print("\n")
print("Nuestros documentos tienen en promedio 294 palabras, aunque estas pueden variar bastante, ya que hay documentos con 2 palabras o 5385. A continuacion se encuentra el testimonio con mas palabras.\n")
max_length = df['Hecho Victimizante'].apply(lambda x: len(str(x))).max()

valor_mas_largo = df[df['Hecho Victimizante'].apply(lambda x: len(str(x))) == max_length]['Hecho Victimizante'].iloc[0]
print("\n")

print(valor_mas_largo)

print("\n")

print("Se trata del relato del alcalde del municipio de Funes, Nariño, durante el período comprendido entre el 1 de enero de 2001 al 31 de diciembre de 2003, donde se describen varios problemas que presentó en su mandato, entre ellos su secuestro y el desplazamiento forzado de algunas familias. Veamos ahora una tabla de frecuencias.\n")

numeros = list(range(2, 6000, 100))

tabfrec = pd.cut(palbrasLong, bins=numeros, include_lowest=True).value_counts().sort_index().reset_index()
tabfrec.columns = ['Intervalo', 'Frecuencia']

print("Tabla de Frecuencias:\n")
print(tabfrec)
print("\n")

print("Vemos que la longitud de los testimonios está sesgada a la derecha. Para confirmar esto, veamos una gráfica que representa la longitud de nuestros textos.\n")

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

sns.histplot(data=palbrasLong, kde=True, ax=axes[0])
axes[0].set_title("Histograma y KDE")

sns.boxplot(data=palbrasLong, ax=axes[1])
axes[1].set_title("Boxplot")

sns.kdeplot(data=palbrasLong, ax=axes[2])
axes[2].set_title("Gráfico de Densidad")

plt.tight_layout()
plt.show()
print("\n")


print("Vemos que nuestra longitud está muy sesgada hacia la derecha. Esto tiene sentido, ya que los testimonios tienden a tener un promedio de 294 palabras, mucho menos que las 5385 que presenta nuestro documento más largo. Hagamos el mismo análisis con el número de caracteres.\n")
palbrasLongChar = palabras.apply(lambda palabra: len(palabra))
print("Descripción a nivel de caracter:\n")
print(palbrasLongChar.describe())
print("\n")

print("Vemos entonces que el texto de 5385 palabras está cerca de los 31854 caracteres. También nuestros textos tienen en promedio 1657 caracteres. Veamos ahora las gráficas correspondientes.\n")
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

sns.histplot(data=palbrasLongChar, kde=True, ax=axes[0])
axes[0].set_title("Histograma y KDE")

sns.boxplot(data=palbrasLongChar, ax=axes[1])
axes[1].set_title("Boxplot")

sns.kdeplot(data=palbrasLongChar, ax=axes[2])
axes[2].set_title("Gráfico de Densidad")

plt.tight_layout()

plt.show()
print("\n")

print("Vemos que nuevamente nuestros textos están sesgados a la derecha a nivel de caracteres. Esto se debe principalmente al sesgo heredado de la distribución de palabras y también a la diferencia entre el promedio y el valor máximo de los datos.\n")
print("Veamos qué relación existe entre la longitud de un texto en palabras y sus caracteres.\n")

from scipy.stats import linregress

slope, intercept, r_value, p_value, std_err = linregress(palbrasLong, palbrasLongChar)

r_squared = r_value ** 2

print("Coeficiente de correlación:", r_value)
print("Intercepto:", intercept)
print("Coeficiente de determinación (R^2):", r_squared)
print("\n")

plt.figure(figsize=(8, 6))
plt.scatter(palbrasLong, palbrasLongChar, color='blue', label='Datos')
plt.plot(palbrasLong, slope * palbrasLong + intercept, color='red', label='Regresión lineal')

plt.title('Relación y Regresión Lineal')
plt.xlabel('Número de palabras')
plt.ylabel('Número de caraceteres')
plt.legend()

plt.show()
