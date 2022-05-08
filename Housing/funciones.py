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
f3 = traduccion(f, traducido)
print("\n")


print("Primero voy a hacer una descripcion general de los datos")
print(f2.describe())
print("En estos datos podemos destacar dos cosas:")
print("1) las medias, en general, se acercan mucho al percentil 50, por lo que podemos suponer que la mayoria de los datos son cercanos a la media. Comprobare esto con las frecuencias")
print("2) Con el maximo y el minimo se observa que hay algunos valores de distorsión, sobre todo en el numero de habitaciones, en la ganancia y en la antigüedad. Estos valores se descartan para futuros analisis.")
print('\n')

print("--------------------------- DISTRIBUCION DE SALARIOS ------------------------")
print("Hemos separado por rangos el salario para ver las frecuencias y su distribucion.")
bins = range(20000, 120000, 5000)
f2["Ganancias Rangos"] = pd.cut(f2["Ganancia Media"], bins)
a = f2.groupby("Ganancias Rangos").agg(frecuencia = ("Ganancia Media", "count"))
print(a)           
ejex = f2["Ganancia Media"]
ejey = bins
plt.hist(ejex, ejey)
plt.savefig("distribucion_ganancias.png")
plt.show()
print("Puede ver la grafica en 'distribucion_ganancias.png'")
print("Como se puede ver en la grafica, se ajusta a una distribucion normal, pero picuda, lo que quiere decir que el rango de valores es estrecho. Estan todos muy cerca de la media.")


print("--------------------------- DISTRIBUCION DE PRECIOS ------------------------")
print("Hemos separado por rangos el precio para ver las frecuencias y su distribucion.")
bins = range(200000, 2500000, 100000)
f2["Rango Precios"] = pd.cut(f2["Precio"], bins)
a = f2.groupby("Rango Precios").agg(frecuencia = ("Precio", "count"))
print(a)
ejex = f2["Precio"]
ejey = bins
plt.hist(ejex, ejey)
plt.savefig("distribucion_precios.png")
plt.show()
print("Puede ver la grafica en 'distribucion_precios.png'")
print("Como se puede ver en la grafica, se ajusta a una distribucion normal.")
print("Esto quiere decir que no hay una diferencia de precios notable. Es decir, no hay casas muy baratas y muy caras, sino que la mayoria tienden a la media.")
print("Esto tiene sentido si lo juntamos con la distribucion de salario, ya que la mayoria de gente ser de clase media, y los precios tienen que ajustarse a las personas, los precios serán tambien medios.")
print('\n')

print("----------------------------PRECIOS POR DISTRITO----------------------")
print("Voy a clasificar las calles por distrito, usando el codigo inicial de cada una.")
codigos = []
for i in range(len(f2.index)):
    cad = str(f2.iloc[i, 6])
    cad = cad.strip()
    codigos.append(str(cad)[0:2])
    
f2["Codigo"] = codigos
    
b = f2.groupby("Codigo").agg(frecuencia = ("Codigo", "count"))
print(b)

d = f2.groupby("Codigo").agg(media_precio = ("Precio", "mean"))
serie = []

for i in range(len(d.index)):
    serie.append(i)

d.insert(loc = 0,column = "Codigo", value = serie)

print(d)

max = d[['media_precio']].max()
print(max)
min = d[['media_precio']].min()
print(min)
diff = max-min
mediaprecios = d[['media_precio']].mean()

plt.bar(d["Codigo"], d["media_precio"])
plt.savefig("Precios_distrito.png")
plt.show()
print("Con esta grafica he intentado averiguar si el precio de la casa varia por zonas. Es decir, si hay un barrio mas caro que otro, etc.")
print("Sin embargo, se observa que las viviendas tienden al mismo precio, variando poco, y no hay una diferencia clara por distritos.")
print("La diferencia entre el precio max y el min es de " + str(diff) + ", que es un porcentaje de " + str((diff/mediaprecios)*100))
print("Esto quiere decir que no hay un aglomeramiento de distintas clases sociales por barrio, sino que estan todos mezclados, siendo la mayoría de clase media.")


print("-----------------------------DISTRIBUCION EDAD DE LA CASA------------------------")
print("Con esto queremos ver si el numero de habitaciones, el precio, y la poblacion dependen la antiguedad de la casa.")
bins = [2, 4, 6, 8, 10]
nombres = ['2-4', '4-6', '6-8', '8-10']
temp = f2
df1 = temp['Edad Casa Media'] = pd.cut(temp['Edad Casa Media'], bins, labels = nombres)
df2 = f2.groupby('Edad Casa Media').mean()
print(df2)


print("--------------------MATRIZ DE CORRELACIONES--------------------")
print("Con la matriz de correlaciones podemos ver si las variables elegidas varian de manera coordinada")
print("He escogido las variables que, a mi parecer, tienen mas relevancia, que son: la ganancia, la antigüedad, el numero de habitaciones y el precio.")
f_corre = f3
#eliminamos las columnas que estorban
f_corre.pop("Num HabitCama Medio")
#f_corre.pop("Poblacion en Area")
f_corre.pop("Direccion")
print(f_corre.corr())
print("Cuanto mas se acerque el 1 o -1 el valor de correlacion, mas relacionadas estan las variables.")
print("Observamos que el precio de la casa esta muy relacionado con el salario, algo bastante intuitivo, con una correlacion de 0.6")
print("Tambien se puede ver que el precio de la casa correlaciona, aunque no mucho, del numero de habitaciones que tenga. Esto tiene una relacion de 0.3")
print("La poblacion en area y el precio de la vivienda tiene una correlacion de 0.4")
print("El ultimo dato interesante es que el precio esta algo relacionado con la edad de la vivienda, con una correlacion de 0.4")
print("El resto de datos muy cercanos al 0, lo que indican que no tienen correlacion ninguna.")