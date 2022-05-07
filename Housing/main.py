import funciones
f = funciones.pd.read_csv("USA_Housing.csv", sep = ',')
print("Este es el dataframe inicial:")
print(f)
print("\n")
funciones.atributos_dataframe(f)
print("\n")
print("En la lista de las columnas podemos observar que todos los nombres estan en ingles.")
print("Para hacer el analisis estadistico mas facilmente, traduciremos estos nombres al español:")
print('\n')
traducido =  {'Avg. Area Income': 'Ganancia Media','Avg. Area House Age':'Edad Casa Media', 'Avg. Area Number of Rooms':'Num Habitaciones Medio', 'Avg. Area Number of Bedrooms': 'Num HabitCama Medio', 'Area Population': 'Poblacion en Area', 'Price':'Precio', 'Address':'Direccion'}
f2 = funciones.traduccion(f, traducido)
print("\n")
print("voy a exportar el dataframe a un excel. De esta manera vere mas facil e intuitivamente la tabla.")
funciones.f2.to_excel("Housing_traducido.xlsx")

print("Voy a hacer distintas graficas con las variables iniciales")
