# TIPOS DE DATOS

edad = 19 
estatura = 1.78
peso = 65.6

print (F"Mi edad es {edad} , mi estatura es {estatura} y mi peso es {peso}")

imc = peso / (estatura * 2)

print ("Su imc es",imc)

print ("Su imc es {:.2f}",format (imc), )

#DATOS DE TIPO DE CADENA DE CARACTERES

asignatura = "Programacion"
carrera = "ICINF"

print ("La asignatura de",asignatura,"corresponde a la carrera de",carrera,)

#LEN FUNCION QUE PERMITE CONTAR CARACTERES


ampolleta = False
interruptor = True

print (ampolleta,interruptor)

print (bool(0))
print (bool(None))
print (bool(True))
print (bool(1))

#LISTAS

nueva_lista = list ()
otra_lista = []

print ("Esta es una lista vacia",nueva_lista,)
print ("Esta es otra lista vacia",otra_lista,)
print (type(otra_lista))

#TIPOS DE LISTAS

estudiantes = ["Pedro", "Juan", "Diego"]
num = [1,2,3,4,5]

print ("Lista de caracteres",estudiantes,)
print ("Lista de numeros",num,)

XD =  list ["Osorno", "Me estai weiando XD", 22, "No puede ser..."]

print ("Hola",XD,)

#SE PUEDEN SUMAR LISTAS

print(f"Listas:{estudiantes}+{num}")

#LEN CUENTA ELEMENTOS DE LA LISTA; COUNT MUESTRA CANTIDAD DE VECES QUE SE REPITE EN LA LISTA

print(len(num))

#INDEX : PARA ELEGIR UN ELEMENTO DE UNA LISTA

numXD = [10, 20, 30, 40]

#PRIMER CARACTER = 0   SEGUNDO CARACTER = 1

print (numXD[0]) # = 10
print (numXD[1]) # = 20

#POSICIONES NEGATIVAS DAN LA VUELTA A LA LISTA

print (numXD[-1]) # = 40
print (numXD[-2]) # = 30

#FORMAT INDICA QUE CANTIDAD DE NUMEROS SALDRAN EN CONSOLA

pi = 3.14159

print ("El valor aproximado de pi es: {:.2f}".format(pi))
print (f"El valor aproximado de pi es: {pi:.2f}")

#EJERCICIO

nombre = input("Ingrese su nombre:")
edad = input("Ingrese su edad:")

print(type(edad))

total_edad = int(edad) + 20

print (f"Hola, mi nombre es {nombre} ,tengo {edad} y en 20 años tendre {total_edad}")

#17 MAYO LABORATORIO 3
#24 AVANCE PROYECTO INTEGRADOR
#31 MAYO PARCIAL 3

listas_XD = list[0,1,2,3,4,5,6,7,8,9]

print (listas_XD)

#TUPLE SON LISTAS QUE NO SE PUEDEN CAMBIAR, SON INVARIABLES, DEFINITIVAS

#SI SE QUIERE CAMBIAR LA TUPLA A VARIABLES, ESTA SE CAMBIA A LISTA

#SETS SON SIMILARES A LISTAS Y TUPLES

#LISTAS []   TUPLAS ()   SETS {}

conjunto_vacio = set()
conjunto_vacio1 = {}

print(type(conjunto_vacio1))

conjunto_colores = set("Rojo")
conjunto_animales = {"Vaca","Cerdo","Oveja","Gallina","Cordero","Perro"}

print("El primer set de colores es:",conjunto_colores)
print("El segundo set de animales es:",conjunto_animales)

#EN SETS NO SE PUEDE CONSULTAR POSICION
#CON ADD PUEDE AGREGAR ELEMENTOS

conjunto_colores.add("Gris")

newtupla = tuple ()
print(newtupla)

datos_personales = [
    Nombre := "Saimon",
    Ciudad := "Osorno",
    Edad_1 := 19,
    Asignatura_1 := "ICINF"
]

print(datos_personales)
print(Nombre)






