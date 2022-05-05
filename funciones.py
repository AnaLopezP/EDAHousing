import pandas as pd

f = pd.read_csv("USA_Housing.csv", sep = ',', header = 0, index_col= 0)
print(f)

def atributos_dataframe(dataframe):
    print("Estas son las filas del dataframe:")
    print(dataframe.index)
    print("Estas son las columnas del dataframe:")
    print(dataframe.columns)

atributos_dataframe(f)
print("")