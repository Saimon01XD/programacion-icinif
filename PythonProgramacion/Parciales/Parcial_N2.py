#EJERCICIO 1

numero = 2
numeros = list()
lista_5 = list()
lista_impar = list()

while numero < 30 :
    print(numero)
    numero += 3
    if numero % 5 == 0 :
        lista_5.append(numero)
    if numero % 2 != 0 :
        lista_impar.append(numero)
    numeros.append(numero)
    
print(numeros)

sumatoria_lista5 = sum(lista_5)
sumatoria_listaImpar = sum(lista_impar)

print("La sumatoria de los enteros divisibles por 5 es: ",sumatoria_lista5)
print("La sumatoria de los enteros impares es: ", sumatoria_listaImpar)

#EJERCICIO 2

nota_lista = list()

def notas() :
    nota = int(input("Ingrese la nota, sin puntos ni comas: "))

    while nota < 10 or nota > 70 :
        nota = int(input("Ingrese una nota valida: "))
    else :
        nota_lista.append(nota)

notas()
notas()
notas()
notas()
notas()
notas()
notas()
notas()
notas()
notas()

print(nota_lista)

cantidad = len(nota_lista)
nota_promedio = (sum(nota_lista)) / cantidad
print(f"El promedio es de :{nota_promedio}")


#EJERCICIO 3

set1 = {100, 250, 300, 1000}
set2 = {150, 250, 500, 1000}

#A 
if 100 in set1 and 100 in set2 :
    print("El valor de 100 esta en ambos sets")
else:
    print("El valor de 100 no esta en ambos sets")

#B
if 500 in set1 or 500 in set2 or 700 in set1 or 700 in set2:
    print("El valor de 500 o 700 se encuentra en uno de los sets")
else:
    print("El valor de 500 o 700 no se encuentra en uno de los sets")

#D
sets = set(set1 + set2)




    