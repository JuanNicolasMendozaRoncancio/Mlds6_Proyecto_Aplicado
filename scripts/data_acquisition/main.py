import pandas as pd

#Importamos nuestro archivo de datos
archivo_inicial = "/content/tdsp_template/docs/data/ArchivoInicialUno.xlsx"
df = pd.read_excel(archivo_inicial)


#Eliminamos las filas sin testimonios y columnas que no presentan información
df = df.dropna(subset=["Hecho Victimizante"]).reset_index(drop=True)

columnas_a_mantener = ['Código Víctima Principal', 'Hecho Victimizante','Fecha Inicio Hecho',
                       'Fecha Fin Hecho','Departament o Hechos','Municipio Hechos',
                       'Lugar Hechos','Bloque']
df = df.filter(items=columnas_a_mantener)



# Generamos una función que divide las filas en segmentos, tal que 
# cada fila de cada uno de los segmentos hable del mismo testimonio
def intervalos(datafra):

  dic = {}  # Diccionario índice fila: índices filas nulas antes de la fila

  # Encuentra los índices de filas no nulas en "Código Víctima Principal"
  no_nulas = [i for i, val in enumerate(datafra["Código Víctima Principal"].notna()) if val]

  # Crea un diccionario de intervalos
  for i in range(len(no_nulas) - 1):
      dic[no_nulas[i]] = list(range(no_nulas[i], no_nulas[i+1]))

  # Asegurémonos de agregar también el último intervalo
  if no_nulas:
      dic[no_nulas[-1]] = list(range(no_nulas[-1], len(datafra)))

  return dic


inter = intervalos(df)

#Implementamos una nueva función para juntar las filas de los segmentos
def juntar(df,inter):
    # Crea un nuevo DataFrame para almacenar el resultado
    resultado = pd.DataFrame(columns=df.columns)

    # Itera a través de los intervalos en el diccionario
    for llave, intervalo in inter.items():
        # Obtiene la primera fila del intervalo
        primera_fila = df.iloc[intervalo[0]]

        # Para las columnas que no son "Hecho Victimizante", toma los valores de la primera fila
        for columna in df.columns:
            if columna != "Hecho Victimizante":
                primera_fila[columna] = df.at[intervalo[0], columna]

        # Para la columna "Hecho Victimizante", concatena los valores que son strings
        hecho_victimizante = " ".join(str(valor) for valor in df.loc[intervalo, "Hecho Victimizante"] if isinstance(valor, str))
        primera_fila["Hecho Victimizante"] = hecho_victimizante

        # Agrega la primera fila del intervalo al DataFrame de resultado
        resultado = resultado.append(primera_fila, ignore_index=True)

    return resultado

dfinal = juntar(df = df, inter = inter)

#Imprimimos un testimonio:
dfinal.at[523, "Hecho Victimizante"]
