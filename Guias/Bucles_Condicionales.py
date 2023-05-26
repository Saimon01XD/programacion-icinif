#4
n = int(input("Ingrese el valor que sera elevado al cuadrado: "))

Nicomaco_Gerasa = list(range(1 , (n * 2), 2))
print(Nicomaco_Gerasa)

sumatoria = sum(Nicomaco_Gerasa)
print("El cuadrado de ", n,"es: ",sumatoria)

#LO DE ARRIBA SIRVE PARA ELEVAR AL CUADRADO, NO AL CUBO

f = int(input("Ingrese el valor que sera elevado al cubo: "))

Gerasa_Real = (f * (f + 1) // 2) ** 2

print(Gerasa_Real)

print("El cubo de ", f," es: ", Gerasa_Real)

