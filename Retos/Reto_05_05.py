

datos_estudiantes = [
    nombre := input("¿Cual es el nombre del estudiante?: "),
    asignatura := input("¿Cual es la asignatura?: "),
    nota_1 := input("¿Cual es la nota Numero 1?: "),
    nota_2 := input("¿Cual es la nota Numero 2?: "),
    promedio := ((int(nota_1)*0.3) + (int(nota_2)*0.7))
]

if (nota_1 := str):
    input("Por favor, introduzca un valor numerico: ")


print("-Nombre:",nombre,
      " -Asignatura:",asignatura,
      " -Nota Numero 1:",nota_1,
      " -Nota Numero 2:",nota_2,
      " -Promedio final:{:.1f}",(promedio)
)