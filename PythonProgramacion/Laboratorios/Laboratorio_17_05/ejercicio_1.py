ID_8 = [
    Nombre_8 := "Bio bio", 
    Superficie_8 := 23890, 
    Habitantes_8:= 1556805
    ]

ID_10 = [
    Nombre_10:= "Los lagos",  
    Superficie_10:= 48583, 
    Habitantes_10 := 828708
    ]

#A
Datos = [
    ID_8,
    ID_10
]
print(Datos)

#B
Densidad_8 = ((Habitantes_8 / Superficie_8))
Densidad_10 = (Habitantes_10 / Superficie_10)

ID_8.insert(-1, Densidad_8)
ID_10.insert(-1, Densidad_10)

print(Datos)

#C
Capital_8 = "Concepcion"
ID_8.insert(-1, Capital_8)
Capital_10 = "Puerto Montt"
ID_10.insert(-1, Capital_10)
print(Datos)

#D
Comunas_8 = ["Lota", "Lebu", "Los Angeles"]
ID_8.insert(-1, Comunas_8)
Comunas_10 = ["Castro", "Puerto Varas", "Purranque"]
ID_10.insert(-1, Comunas_10)
print(Datos)

#E
Provincias_8 = ("Biobio", "Arauco", "Concepcion")
ID_8.insert(-1, Provincias_8)
Provincias_10 = ("Osorno", "Chiloe", "LLanquihue", "Palena")
ID_10.insert(-1, Provincias_10)

print(Datos)






