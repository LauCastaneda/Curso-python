#Variable de texto
mi_variable = "HolaMiNombreEsLaura"
print(mi_variable)

#Lista de número
mi_lista = [8,10,12,14]
print(mi_lista)

#diccionario para dar etiqueta a un valor, por ejemplo etiquetar mujer=1 hombre=0
mi_diccionario = {"Nombre" : "Lau", "Edad" : "21", "Mascota" : "Luna"}
print(mi_diccionario)

#la edad no es un numero entero, puede ser 25.5 que son 25 años y 5 meses
#este vector repite 5 veces mi valor
vector_de_enteros = [1250]*1
print(vector_de_enteros)

#vector de decimales o flotantes
vector_de_flotantes = [3.5698]*5
print(vector_de_flotantes)

#creamos un diccionario
diccionario0 = {"entero" : vector_de_enteros, "flotantes" : "vector_de_flotantes", "complejos" : vector_de_flotantes}
print(diccionario0)

#Cadenas
cadena_simple = "Hola a todos"
cadena_doble = ["CocaCola", "es deli"]
print(cadena_doble)

#Dataframe - librería pandas 
#estructura de datos con dos dimensiones columnas variables filas obs
#Siempre empieza desde cero
import pandas as pd

#importar datos
imp_sri =pd.read_excel("data/ipc.xlsx")
print(imp_sri)