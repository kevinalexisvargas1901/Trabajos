# Operadores
variableX = 5
variableY = 10

variableZ, variableW = 8, 7

print(f" variableX == variableY: {variableX == variableY} ") # respuesta logica --> True o False
print(f" variableZ != variableW: {variableW != variableZ} ") # respuesta logica --> True o False
print(f" variableY > variableW: {variableY > variableW} ") # respuesta logica --> True o False
print(f" variableX < variableZ: {variableX < variableZ} ") # respuesta logica --> True o False
print(f" variableW >= variableY: {variableW >= variableY} ") # respuesta logica --> True o False
print(f" variableZ <= variableW: {variableZ <= variableW} ") # respuesta logica --> True o False

"""
    Operadores lógicos
    
    and, or, not
   
"""

tiene_saldo = True
esta_libre = False

print(f"AND: {tiene_saldo and esta_libre}")
print(f"OR: {tiene_saldo or esta_libre}")
print(f"not: {not esta_libre}")

#nombre = "Kevin"
#apellido = "Vargas"
#edad = 18

#print(f"Nombre: {nombre}, Apellido: {apellido}, Edad: {edad}")

edad = input ("Ingrese un número: ")

if edad.isdigit():
    edad = int (edad)
    print(f"La edad es valida: {edad}")
else:
    print(f"Error, por favor ingrese un numero entero positivo")

tiene_dinero = True

if tiene_dinero:
    print(f"Salgamos este viernes")
else:
    print (f"Te deseo éxitos")
    
    #EJERCICIO
    
tiene_cedula = True
es_estudiante = True
es_soltero = True

if tiene_cedula:
    print(f"Usted es mayor de edad")
else:
    print (f"Usted no es mayor de edad")
    
if es_estudiante:
    print(f"Usted es un estudiante")
else:
    print (f"Usted no es un estudiante")
  
if es_soltero:
    print(f"Usted está soltero")
else:
    print (f"Usted no está soltero")

#EJERCICIO

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num1 > num2:
    print(f"El numero 1 es mayor que el numero 2")
if num1 < num2:
    print(f"El número 1 es menor que el número 2")
if num1 == num2:
    print(f"Los números son iguales")

"""
EJERCICIOS

Ejercicio 1: Verificar mayoría de edad
1. Enunciado:
Pide la edad de una persona y muestra un mensaje si es mayor de edad (18 años o más).


2. Ejercicio 2: Determinar si un número es positivo
Enunciado:
Pide un número y muestra un mensaje si el número es positivo.

3. Ejercicio 3: Verificar rango de valores

Enunciado:
Pide un número y muestra un mensaje solo si está entre 10 y 50 (inclusive).
"""
edad = int(input("Ingrese su edad"))
if edad < 18:
    print(f"Usted es meno de edad")
elif edad > 18:
    print (f"Usted es mayo de edad")