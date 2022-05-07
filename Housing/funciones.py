import pandas as pd
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
print(traduccion(f, traducido))
print("\n")
print("Una vez hecho esto, vamos a visualizar mediante graficas las variables")