import pandas as pd
import numpy as np




# Dataframe que contiene solo el dataset de las plaformas.
df_data = pd.read_csv('data_titles.csv')

# Dataframe que contiene todo la informacion.
#df_data_total = pd.read_csv('data_total.csv')
df_data_total = pd.read_csv('data_score_titles.csv')



### QUERY 1:
''' Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN.
(la función debe llamarse get_max_duration(año, plataforma, duración_tipo)) '''

def get_max_duration( plataforma, tipo_duracion, año):

    df_aux  = df_data [ plataforma[0] == df_data.id.str[0]]

    df = df_aux[(df_aux.release_year == año  )& (df_aux.duration_type == tipo_duracion)].sort_values('title', ascending = True)
    
    df = df[df.duration_int == df.duration_int.max()]

    return df.iloc[0,2], df.iloc[0,9]




### QUERY 2: 

'''Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año'''

def get_score_count(plataforma, puntaje , año ):

    df_aux  = df_data_total [ plataforma[0] == df_data_total.id.str[0]]
    cantidad = len(df_aux[ (df_aux.score > puntaje ) & (df_aux.release_year == año)])

    return  cantidad



###  QUERY 3: 
''' Cantidad de películas por plataforma con filtro de PLATAFORMA. 
(La función debe llamarse get_count_platform(plataforma)) '''

def get_count_platform(plataforma ):

    df_aux  = df_data [ plataforma[0] == df_data.id.str[0]]
    return  len(df_aux)



###  QUERY 4: 
''' Actor que más se repite según plataforma y año. (La función debe llamarse get_actor(platform, year))''' 

def get_actor(plataforma, año ):

    lista = []
    lista_split = []

    df_aux  = df_data [ plataforma[0] == df_data.id.str[0]]
    df = df_aux[df_aux.release_year == año]

    for i in df.cast:
        if i is np.nan: 
            continue
        lista.append(i)
        
    for i in lista:
        for j in i.split(','):
            lista_split.append(j.strip())

    actor = max(set(lista_split), key = lista_split.count)
    
    return actor



