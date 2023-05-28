numero = int(input("Ingrese el numero que desee: "))

if (numero % 2) == 0 :
    print("Este numero es par")
else :
    print("Este numero es impar")

if numero < 50 :
    print("Este numero es menor a 50")
else :
    print("Este numero es mayor a 50")

#PRIMO ES SOLO DIVISIBLE POR 1 Y EL MISMO NUMERO (X)

def primo(numero) :

    if numero < 2 :
        return False
    for i in range(2, int(numero ** 0.5) + 1) :
        if numero % i == 0 :
            return False
    return True

if primo(numero) :
    print("El numero es primo")
else :
    print("El numero no es primo")    