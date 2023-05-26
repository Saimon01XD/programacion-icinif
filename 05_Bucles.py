edad = 15
num = 0

#while edad < 18 :
#    print("Eres menor de edad, no puedes manejar")         #NO EJECUTAR

##CTRL + C PARA TERMINAR PROCESO

#while True :
#    print(num)
#    num += 2           #NO EJECUTAR

##num += 2 ES LO MISMO QUE num = num + 2

while num <= 100:
    print(num)
    num += 2
    if num == 50 :
        print("Llegaste a 50")
print("Fin del bucle N°1")

while num <= 200 :
    print(num)
    num += 2
    if num == 150 :
        print("Se detiene el proceso")
        break
print(num)
print("Fin del bucle N°2")              #BREAK SE UTILIZA DENTRO DE CICLOS, NO DE IF/ELSE

#LA SIGUIENTE FUNCION: IMPRESION DE UNA LISTA DE ELEMENTOS DE MANERA VERTICAL

for i in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) :
    print(i)                                #ESTO NO ESTA BIEN OPTIMIZADO, SE HARIAN CON LISTAS YA CREADAS

nueva_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in nueva_lista :                      #i SERIA ITERAR
    print(i)

for i in range(11) :                        
    print(i)
for i in range(1, 11) :                     #LAS DOS FUNCIONES SON LO MISMO
    print(i)

