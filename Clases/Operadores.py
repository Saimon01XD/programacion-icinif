#SE PUEDEN MULTIMPLICAR STRINGS

print ("Hola mundo!" *5)

#OPERADORES MATEMATICOS
a = 2
b = 5

print (a > b) #a MAYOR QUE b
print (a < b) #a MENOR QUE b
print (a == b) #a IGUAL A b
print (a != b) #a DISTINTO A b
print (a >= b) #a MAYOR O IGUAL A b
print (a <= b) #a MENOR O IGUAL A b

#COMPARANDO VARIABLES DE STRINGS

gato_domestico = "gato"
gato_salvaje = "puma"
#ESTO SIEMPRE DROPEARA TRUE O FALSE
print ((len(gato_domestico)) == (len(gato_salvaje)))
print (gato_domestico != gato_salvaje)
print (gato_domestico > gato_salvaje)
print (gato_domestico < gato_salvaje)

#CONDICIONALES IF/OR/ELSE

bencina = True
encendido = True
edad = 19

#OPERADOR AND 
if bencina and encendido:
    print("El vehiculo puede avanzar")
else:
    print("El vehiculo no puede avanzar")

#OPERADOR OR
if bencina or encendido:
    print("El vehiculo puede avanzar")
else:
    print("El vehiculo no puede avanzar")

#OPERADOR NOT / TRUE = FALSE / FALSE = TRUE / LO tRANSFORMA A FALSO O VERDADERO
if not bencina and encendido:
    print("El vehiculo puede avanzar")
else:
    print("El vehiculo no puede avanzar")

#CAGUE
if not bencina or (encendido and edad >= 18):
    print("El vehiculo puede avanzar")
else:
    print("El vehiculo no puede avanzar")
