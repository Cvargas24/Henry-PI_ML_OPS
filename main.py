
import pandas as pd
import numpy as np

import queries

from fastapi import FastAPI
from enum import Enum


app = FastAPI()


class plataforma(str, Enum):
    amazon = "amazon"
    disney = "disney"
    hulu = "hulu"
    netflix = 'netflix'



@app.get("/models/{plataforma}")
async def get_model(platform: plataforma):
    return f'mi plataforma es: {platform}'




# Query 1: 
@app.get('/get_word_count/{platform}/{anio}/{duration_type}')
async def get_max_duration(  platform : plataforma, anio: int, duration_type: str):
    movie = queries.get_max_duration( platform, duration_type, anio)

    return f'La pelicula con mayor duracion en el año {anio} en {platform} es: {movie[0]} con un total de {movie[1]} {duration_type}'




# Query 2:
@app.get('/get_score_count/{platform}/{scored}/{anio}')
async def get_score_count( platform: plataforma, scored: float, anio : int):
    count_movie = queries.get_score_count(platform, scored, anio)

    return f'La cantidad total de peliculas de la plataforma {platform} con puntaje mayor a {scored} en el año {anio} es: {count_movie}'


# Query 3:
@app.get('/get_count_platform/{platform}')
async def get_count_platform( platform: plataforma):
    count_movie = queries.get_count_platform(platform)

    return f'La cantidad total de peliculas en la plataforma {platform} es: {count_movie}'


# Query 4:
@app.get('/get_actor/{platform}/{anio}')
async def get_actor( platform: plataforma, anio : int):
    actor = queries.get_actor(platform, anio)

    return f'El actor que mas se repite en {platform} en el año {anio} es: {actor}'







