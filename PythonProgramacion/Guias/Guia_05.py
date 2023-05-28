########## RECORDAR QUITAR # AL QUERER TRABAJAR CON LOS EJERCICIOS

###EJERCICIO N°1

a = int(input("Ingrese el primer digito: "))
b = int(input("Ingrese el segundo digito: "))
c = int(input("Ingrese el tercer digito: "))

lista = [A, B, C]

lista.sort()

print(f"El orden de menor a mayor es {lista}")

####EJERCICIO N°2
palabra_1 = str(input("Ingrese su primera palabra: "))
palabra_2 = str(input("Ingrese su segunda palabra: "))

palabra_1 = len(palabra_1)
palabra_2 = len(palabra_2)

cadena = [palabra_1, palabra_2]

print(cadena)     ###FALTA TRABAJARLO

####EJERCICION N°3
x = int(input("Ingrese el lado A: "))
y = int(input("Ingrese el lado B: "))
z = int(input("Ingrese el lado C: "))

if X == Y and X == Z and Y == Z :
    print("El triangulo es equilatero")
if X == Y and X != Z or X == Z and X != Y or Y == Z and Y != X :
    print("El triangulo es isoceles")
if X != Y and X != Z and Y != Z :
    print("El triangulo es escaleno")

formula_heron = (X + Y + Z) / 2
area_triangulo = (formula_heron*(formula_heron - X)*(formula_heron - Y)*(formula_heron - Z))**0.52

print(area_triangulo)

####EJERCICIO N°4
nombre_1 = str(input("Ingrese su nombre: "))
nombre_2 = str(input("Ingrese el otro nombre: "))

if nombre_1[0] == nombre_2[0] :
    print("Ambos nombres comienzan con la misma letra")
if nombre_1[-1] == nombre_2[-1] :
    print("Ambos nombres terminan con la misma letra")

####EJERCICIO N°5
print("Por favor, ingrese las notas sin puntos ni comas")
nota_1 = int(input("Ingrese la nota 1 del laboratorio: "))
nota_2 = int(input("Ingrese la nota 2 del laboratorio: "))
nota_3 = int(input("Ingrese la nota 3 del laboratorio: "))

ponderado = (nota_1 * 0.3) + (nota_2 * 0.4) + (nota_3 * 0.3)

if ponderado < 40 :
    print("El estudiante reprobo la asignatura")  
if (40 < ponderado) < 60 :
    print("El estudiante aprobo la asignatura")
if 60 < ponderado :
    print("El estudiante aprobo con distincion la asignatura")

####EJERCICIO N°6
grupo_1 = {"Marcos", "Gabriela", "Benjamin", "Matias"}
grupo_2 = {"Marcos", "Nicolas", "Diego", "Matias"}

repetidos = grupo_1 & grupo_2
print(repetidos)

####EJERCICIO N°7
trabajadores_1 = ["Pedro", "Juan", "Diego", "Gabriel", "Gabriela"]
edad_trabajadores = [21, 35, 48, 15, 32]

trabajadores_edad = list(zip(trabajadores_1, edad_trabajadores))

print(trabajadores_edad)

####EJERCICIO N°8
mes = str(input("Introduzca el mes que desee: "))

if mes == "Diciembre" or mes == "Enero" or mes == "Febrero" :
    print("Es verano!")
if mes == "Marzo" or mes == "Abril" or mes == "Mayo" :
    print("Es otoño!")
if mes == "Junio" or mes == "Julio" or mes == "Agosto" :
    print("Es invierno!")
if mes == "Septiembre" or mes == "Octubre" or mes == "Noviemre" :
    print("Es primavera!")

####EJERCICIO N°9
numeros = [4, 3, 8, 12, 6, 10, 14, 3, 6]

del numeros[-1]
print(numeros)

numeros.insert(0,2)  #PA LOS NUMEROS INSERT VA MAS PIOLA QUE ADD(ADD ES PA AGREGAR SIN ORDEN), [x. y] x es posicion, y es elemento
print(numeros)

sin_duplicados = list(set(numeros))   #LIST(SET()) SIRVE PA ELIMINAR ELEMENTOS REPETIDOS Y EL LIST ME LO DEVUELVE DNUEVO COMO LISTA
print(sin_duplicados)

numeros_ordenados = sorted(numeros) #SORTED ME ORDENA LOS DATOS DE MENOR A MAYOR
numeros_cantidad = len(numeros) #LEN ME DIRA CUANTOS CARACTERES TIENE MI CONJUNTO

suma_numeros = sum(numeros_ordenados) #SUM ME SUMA (XD) LOS ELEMENTOS DENTRO DE LA LISTA QUE PEDI

media = (suma_numeros / numeros_cantidad)

if (numeros_cantidad % 2) == 0 :
    mediana = int((numeros_cantidad / 2))
    print(mediana)
else :
    mediana = ((numeros_cantidad + 1) / 2)
    print(mediana)

print(media)
print(mediana)

####EJERCICIO N°10
agenda = [
    nombre := "X",
    direccion := "Y",
    ciudad := "Z",
    numero_telefonico := "A"
]

agenda.add(redes_sociales := "B", "C", "D")

red_social_B = agenda["B"]
print(red_social_B)