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
print("voy a exportar el dataframe a un excel. De esta manera vere mas facil e intuitivamente la tabla.")
f2.to_excel("Housing_traducido.xlsx")

print("Voy a hacer distintas graficas con las variables iniciales")
print("1) histograma de la ganancia")
fig = plt.figure()
ejex = [0, 10000, 20000, 300000, 400000, 500000, 600000, 700000]
ejey = [0, 50, 100, 150, 200, 250, 300, 350, 400]

plt.hist(ejex, ejey, color = "b")
plt.savefig("Histograma Ganancias.jpg")
plt.show()