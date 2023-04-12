#COMENTARIO DE UNA LINEA
#ESTE TEXTO SIRVE PARA GUIAR , NO SE EJCUTA

#01 SIMPLE PRINT
print ("Hola mundo")

#02 DECLARANDO VARIABLE
nombre = "Saimon"
name = "Constanza"

#03 IMPRIMIENDO VARIABLES
print (name)
print ("Hola soy",nombre)
#LA COMA ARRIBA SEPARA LA VARIABLE DEL TEXTO NOMAS

#04 DEFINIENDO VARIABLE TIPO NUMERICO
edad = "19"
#PARA ENTEROS ES INT; PARA N°IMAGINARIOS ES COMPLEX Y FLONT PARA 

#05 IMPRIMIENDO VARIABLE TIPO NUMERICO
print ("Mi edad es de",edad)

#06 IMPRIMIENDO 2 VARIABLES EN LA MISMA LINEA
print ("Hola, mi nombre es",nombre,"y tengo",edad,"años")
print (f"Hola, mi nombre es {nombre} y tengo {edad} años")
print (F"Hola, mi nombre es {nombre} y tengo {edad} años")
#STR SERVIRIA PARA TRANSFORMAR NUMEROS A TEXTO, PUEDE QUE NO DEJE MEZCLAR VARIABLES DE TEXTO Y NUMEROS(ESTO SIRVE CUANDO UTILIZO + en vez de comas,)

#07 ACTUALIZANDO LA VARIABLE NOMBRE (MUTABLE)
nombre = "Animan"

#08 IMPRIMIENDO NUEVA VARIABLE
print ("Hola, mi nuevo nombre es",nombre)

#09 VARIABLES EN UNA SOLA LINEA (NO RECOMENDADO)
ciudad, pais, region, year ="Osorno","Chile","Los Lagos","2023"
print ("Yo vivo en la ciudad de",ciudad,",en el pais de",pais,"en la region de",region,",actualmente en",year,)

#10 UTILIZANDO INSTRUCCION INPUT
nombre1 = input ("Cual es tu nombre?")
edad1 = input ("Cual es tu edad?")
#INPUT SIRVE PARA PEDIR INFORMACION AL USUARIO