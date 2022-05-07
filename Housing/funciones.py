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

f = pd.read_csv("USA_Housing.csv", sep = ',')
print("Este es el dataframe inicial:")
print(f)
print("\n")
atributos_dataframe(f)
print("\n")
print("En la lista de las columnas podemos observar que todos los nombres estan en ingles.")
print("Para hacer el analisis estadistico mas facilmente, traduciremos estos nombres al español:")
print('\n')
traducido =  {'Avg. Area Income': 'Ganancia Media','Avg. Area House Age':'Edad Casa Media', 'Avg. Area Number of Rooms':'Num Habitaciones Medio', 'Avg. Area Number of Bedrooms': 'Num HabitCama Medio', 'Area Population': 'Poblacion en Area', 'Price':'Precio', 'Address':'Direccion'}
f2 = traduccion(f, traducido)
print("\n")
'''print("voy a exportar el dataframe a un excel. De esta manera vere mas facil e intuitivamente la tabla.")
f2.to_excel("Housing_traducido.xlsx")'''

print("Primero voy a hacer una descripcion general de los datos")
print(f2.describe())

print("--------------------------- DISTRIBUCION DE SALARIOS ------------------------")
print("Hemos separado por rangos el salario para ver las frecuencias y su distribucion.")
bins = range(20000, 120000, 5000)
f2["Ganancias Rangos"] = pd.cut(f2["Ganancia Media"], bins)
a = f2.groupby("Ganancias Rangos").agg(frecuencia = ("Ganancia Media", "count"))
print(a)
ejex = f2["Ganancia Media"]
ejey = bins
plt.hist(ejex, ejey)
plt.show()
print("Como se puede ver en la grafica, se ajusta a una distribucion normal.")

print("--------------------------- DISTRIBUCION DE PRECIOS ------------------------")
print("Hemos separado por rangos el precio para ver las frecuencias y su distribucion.")
bins = range(200000, 2500000, 100000)
f2["Rango Precios"] = pd.cut(f2["Precio"], bins)
a = f2.groupby("Rango Precios").agg(frecuencia = ("Precio", "count"))
print(a)
ejex = f2["Precio"]
ejey = bins
plt.hist(ejex, ejey)
plt.show()
print("Como se puede ver en la grafica, se ajusta a una distribucion normal.")
