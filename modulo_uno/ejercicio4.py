opcion = ""

print("******MENU POR CONSOLA******")
print("1. Saludar")
print("2. Mensaje")
print("3. Salir")

while True:
    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        print("Hola, cómo estas?")
    elif opcion == "2":
        print("Ojos que no ven, corazón que no siente")
    elif opcion == "3":
        print("Saliendo...")
        break
    
suma = 0

while numero !=0:
    numero = int(input("Ingrese un numero, ingrese el 0 para salir"))
    suma += numero
    
print(f"La suma es => {suma}")

# Desarrolle una app en python que permita sumar los números de 1 al 100

for suma in range(1, 101):
    print(f"{suma}")


# Desarrolle una app en python que permita calcular el cuadrado de los números de 1 al 5

for resultado in range(1, 6):
    cuadrado = resultado ** 2
    print(f"{cuadrado}")


# Desarrolle una app en python que permita mostrar solo las vocales de una palabra

palabra = input("\n\nIngrese la palabra para extraer las vocales: ")
vocales = "aeiouAEIOU"

for letras in palabra:
    if letras in vocales:
        print(f"Las vocales encontradas fueron: {letras}")


# Desarrolle una app en python que permita imprimir la tabla de multiplicar de un número ingresado por teclado

multiplicacion = int(input("Escriba el número que requiera ver la tabla de multiplicar: "))

for escala in range(1, 11):
    resultado = multiplicacion * escala
    print(f"{multiplicacion} x {escala} = {resultado}")
