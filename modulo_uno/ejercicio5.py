###  **Ejercicios básicos con funciones `def`**

#1. **Suma de dos números**
#   Crea una función que reciba dos números y retorne su suma.

numero1 = int(input("Digite el primer número: "))
numero2 = int(input("Digite el segundo número: "))

def sumar(numero1, numero2):
    print(f"La suma de {numero1} + {numero2} = {numero1+numero2}")
    
sumar(numero1,numero2)

#2. **Número par o impar**
#   Escribe una función que reciba un número y diga si es par o impar.

numero = int(input("Digite su número: "))

def par_impar(numero):
    if numero %2 == 0:
        print(f"El numero {numero} es un número Par")
    else:
        print(f"El numero {numero} es un número Impar")

par_impar(numero)

#3. **Área de un triángulo**
#   Pide base y altura y devuelve el área del triángulo.
#  *(Fórmula: base × altura / 2)*

base = int(input("Digite la base del triángulo: "))
altura = int(input("Digite la altura del triángulo: "))

def area(base, altura):
    print(f"El área del tríangulo de base {base} y de altura {altura} es de {int((base*altura)/2)}")

area(base,altura)

#4. **Saludo personalizado**
#   Crea una función que reciba el nombre de una persona y devuelva un saludo como `"Hola, <nombre>!"`.

nombre = str(input("Ingrese su nombre: "))

def saludo(nombre):
    print(f"Hola {nombre}, Bienvenido")

saludo(nombre)

#5. **Máximo de tres números**
#   Define una función que reciba tres números y retorne el mayor.

num1 = int (input("Ingrese el primer número: "))
num2 = int (input("Ingrese el segundo número: "))
num3 = int (input("Ingrese el tercer número: "))

def maximo(num1, num2, num3):
    print(f"El número mayor entre {num1}, {num2}, {num3} es: {max(num1,num2,num3)}")

maximo(num1, num2, num3)

#6. **Contar vocales en una palabra**
#   La función debe contar cuántas vocales hay en una cadena dada.

palabra = str(input("Ingrese su palabra: "))

def contar_vocales(palabra):
    contVocales = 0
    vocales = "aeiou"
    for letras in palabra:
        if letras in vocales:
            contVocales += 1
    
    print(f"En la palabra {palabra} hay {contVocales} vocales")

contar_vocales(palabra)

#7. **Convertir grados Celsius a Fahrenheit**

#8. **Verificar si una palabra es palíndromo**
#   Una función que determine si una palabra se lee igual al derecho y al revés.
#[::-1]
#9. **Contar elementos pares en una lista**
#   La función recibe una lista de números y devuelve cuántos son pares.

#10. **Calculadora básica**
#    Crea una función que reciba dos números y una operación (`"suma"`, `"resta"`, `"multiplicación"`, `"división"`) y devuelva el resultado correspondiente.
