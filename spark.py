import pandas as pd
import numpy as np


from pyspark.sql import SparkSession
from pyspark.sql.functions import avg
from pyspark.sql.functions import round




def create_df_score(file_name):
    ''' 
    Recibe la ruta del archivo .csv que se desea convertir. 
    Devuelve un dataframe que contiene el calculo del promedio de rating(score) agrupados por "id" 
    
    Ejm:    +------+------------------+
            |    id|             score|
            +------+------------------+
            |ns8641|               3.5|
            |as1586|3.4768421052631577|
            |hs1299|3.5724489795918366|
    
    '''

    # Crea una sesion para Spark
    spark = SparkSession \
                .builder \
                .appName("Python Spark SQL basic example") \
                .config("spark.some.config.option", "some-value") \
                .getOrCreate()



    data_spark = spark.read.csv(file_name, header = True)
    spark_total = data_spark.groupBy("id").agg( round(avg('rating'),4).alias('score') )
    
    # Convierte a dataframe. 
    df = spark_total.toPandas()

    return df







