#Temperatura

temperatura = int(input("Por favor, ingrese la temperatura: "))

if temperatura < 0:
    print("Hace mucho frío")
elif temperatura <= 20:
    print ("Clima templadito")
elif temperatura <= 30:
    print("Clima agradable")
else:
    print ("La temperatura es Terrible...")
"""
Ejercicios:

1. Número positivo, negativo o cero

Descripción: Solicitar un número e indicar si es positivo, negativo o cero.

2. Clasificador de notas

Descripción: El usuario ingresa una nota de 0 a 100. Mostrar el nivel académico según el puntaje.

| Rango  | Mensaje   |
| ------ | ----------|
| 90–100 | Excelente |
| 70–89  | Aprobado  |
| 0–69   | Reprobado |


3. Clasificador de edad

Descripción: Pedir la edad del usuario y clasificarla en rangos.

| Rango | Mensaje      |
| ----- | ------------ |
| 0–12  | Niño         |
| 13–17 | Adolescente  |
| 18–59 | Adulto       |
| 60+   | Adulto mayor |


5. Verificar hora del día

Descripción: Pedir la hora (0 a 23) e indicar si es mañana, tarde o noche.
"""
#Mayor de edad

edad = int(input("Ingrese su edad"))

if edad < 18:
    print("Usted es menor de edad")
else:
    print ("Usted es mayor de edad")
    
#Numero Positivo, Negativo o Cero

numero = int(input("Ingrese su número: "))

if numero < 0:
    print("Su número es negativo")
elif numero == 0:
    print("Su número es igual a cero")
else:
    print("El número es positivo")
    
#Clasificador de notas

nota = int(input("Ingrese su nota: "))

if nota < 70:
    print("Reprobado")
elif nota < 90:
    print("Aprobado")
elif nota < 101:
    print("Excelente")
    
#Clasificador de edad

edad = int(input("Ingrese su edad: "))

if edad < 13:
    print("Niño")
elif edad < 18:
    print("Adolescente")
elif edad < 60:
    print("Adulto")
elif edad > 60:
    print("Adulto Mayor")
    
#Hora

nota = int(input("Ingrese la Hora: "))

if nota < 12:
    print("Mañana")
elif nota < 18:
    print("Tarde")
elif nota < 24:
    print("Noche")