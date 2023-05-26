#ELIF ES AGREGAR UNA TERCERA U OTRA OPCION A LA CADENA IF/ELSE

edad = 66

if edad >= 18 and edad < 65 :
    print("Eres mayor de edad")
elif edad >= 65 :
    print("Eres un adulto mayor")
else:
    print("Eres menor de edad")

#FOR INDICA LA CANTIDAD DE VECES QUE QUIERO QUE SE REALIZE LA FUNCION
#WHILE INDICA QUE SE REPETIRA HASTA QUE SE CUMPLA LA CONDICION

num = 0

while num <= 100 :
    print(num)
    num += 2

#SI UTILIZO CICLO INFINITO = CTRL + C PARA DETENER EL PROCESO / O CERRAR TOD0!!!!

#NO IMPRIMIR

#while True :
 #   print(num)
  #  num += 2

#WHILE TAMBIEN SE PUEDE COMBINAR CON ELSE/IF

while num <= 100 :
    print(num)
    num += 2
else :
    print("MI condicion es igual o mayor a cien")

#BREAK ME CERRARA EL COMANDO WHILE

while True :
    parametro = input(">")
    if parametro == "exit" :
        break
    else :
        print(parametro)        #ESTE LOOP PIDE PALABRAS PARA IMPRIMIRLAS, HASTA QUE EL USUARIO INGRESE LA PALABRA CLAVE, EN ESTE CASO EXIT

#== ME COMPARA / = ME ASIGNA / PARA IF/ELSE CON VARIABLES TRUE/FALSE SE USA = PARA ASIGNARLE Y NO COMPARAR; ESTO PARA TRUE Y FALSE