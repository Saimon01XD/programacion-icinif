a = [10, 9, 12, 15, 18]
b = [21, 8, 15, 13, 12]

#A
a_y_b = a + b
print(a_y_b)

#B
a_y_b.insert(-9, 30)
print(a_y_b)

#C
lista_ordenada = list(set(a_y_b))
print(lista_ordenada)

#D
d = [4, 5, 6]
nueva_lista_ordenada = lista_ordenada + d
print(nueva_lista_ordenada)

#E
suma_lista = sum(nueva_lista_ordenada)
print(suma_lista)

#F
cantidad_numeros = len(nueva_lista_ordenada)

media = (suma_lista / cantidad_numeros)

if cantidad_numeros % 2 == 0 :
    mediana = (cantidad_numeros / 2)
if not cantidad_numeros % 2 == 0 :
    mediana = (cantidad_numeros + 1) / 2

print(media)
print(mediana)


