########## RECORDAR QUITAR # AL QUERER TRABAJAR CON LOS EJERCICIOS

###EJERCICIO N°1

a = input("Ingrese el primer digito: ")
b = input("Ingrese el segundo digito: ")
c = input("Ingrese el tercer digito: ")
A = int(a)
B = int(b)
C = int(c)

lista = [A, B, C]

lista.sort()

print(f"El orden de menor a mayor es {lista}")

####EJERCICIO N°2
palabra_1 = input(str("Ingrese su primera palabra: "))
palabra_2 = input(str("Ingrese su segunda palabra: "))

palabra_1 = len(palabra_1)
palabra_2 = len(palabra_2)

cadena = [palabra_1, palabra_2]

print(cadena)     ###FALTA TRABAJARLO

####EJERCICION N°3
x = input("Ingrese el lado A: ")
y = input("Ingrese el lado B: ")
z = input("Ingrese el lado C: ")
X = int(x)
Y = int(y)
Z = int(z)

if X == Y and X == Z and Y == Z :
    print("El triangulo es equilatero")
if X == Y or X == Z or Y == Z :
    print("El triangulo es isoceles")
if X != Y and X != Z and Y != Z :
    print("El triangulo es escaleno")

formula_heron = (X + Y + Z) / 2
area_triangulo = (formula_heron*(formula_heron - X)*(formula_heron - Y)*(formula_heron - Z))**0.52

print(area_triangulo)

####EJERCICIO N°4
nombre_1 = input("Ingrese su nombre: ")
nombre_2 = input("Ingrese el otro nombre: ")
nombre_1 = str(nombre_1)
nombre_2 = str(nombre_2)

if nombre_1[0] == nombre_2[0] :
    print("Ambos nombres comienzan con la misma letra")
if nombre_1[-1] == nombre_2[-1] :
    print("Ambos nombres terminan con la misma letra")

####EJERCICIO N°5
print("Por favor, ingrese las notas sin puntos ni comas")
nota_1 = input("Ingrese la nota 1 del laboratorio: ")
nota_2 = input("Ingrese la nota 2 del laboratorio: ")
nota_3 = input("Ingrese la nota 3 del laboratorio: ")
nota_1 = int(nota_1)
nota_2 = int(nota_2)
nota_3 = int(nota_3)

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
mes = input("Introduzca el mes que desee: ")
mes = str(mes)

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

suma_numeros = sum(numeros_ordenados)

media = (suma_numeros / numeros_cantidad)
mediana = ((numeros_cantidad + 1) / 2)
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











