#Tuplas
#lista = []
#tuplas = ()
#lista[tuplas()]

colores = ("amarillo", "azul", "rojo")
print(colores[2])
print(colores[1])

#tupla con valores diferentes
personal = ("Juan Pablo", 22, True)
print(personal[0])
print(personal[2])

for color in colores:
    print(color)
    
#Desempaquetado de tuplas
nombre, edad, edo_civil = personal
print(nombre)
print(edad)
print(edo_civil)

#Tratando de modificar una tupla
persona = ("Juan Pablo", 22, True)

#persona[1] = 29 #error

#Slice

ventas_mensuales = [12000, 9800, 10200, 14500, 16000, 13200, 11000, 11700, 9800, 10500, 14000, 13800]

for venta in enumerate(ventas_mensuales, start = 1):
    print(venta)
    
ventas_T2 = ventas_mensuales[3:6]

ventas_top = [v for v in ventas_mensuales if v >13000]
print(f"Ventas del segundo trimestre {ventas_T2}")
print(f"Ventas Top {ventas_top}")
