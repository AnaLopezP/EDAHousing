import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
def atributos_dataframe(dataframe):
    print("Estas son las filas del dataframe:")
    print(dataframe.index)
    print("Estas son las columnas del dataframe:")
    print(dataframe.columns)

def traduccion(dataframe, lista):
    dataframe = dataframe.rename(columns = lista)
    return dataframe





