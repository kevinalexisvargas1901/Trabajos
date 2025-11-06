# input() = +, -, *, /, datos alfabeticos 

numero_uno = int(input("Por favor, ingrese un número: "))
numero_dos = int(input("Por favor, ingrese otro número"))

print ("Por favor, seleccione o ingrese el operador de la calculadora: +, -, *, /")
opcion = input("Seleecione un operador: ")

# Condicionales: if, if-elif-else

if opcion == "+":
    print(f"Resultado de la suma = {numero_uno + numero_dos}")
elif opcion == "-":
    print (f"Resultado de la resta = {numero_uno - numero_dos}")
elif opcion == "*":
    print (f"Resultado de la multiplicación = {numero_uno * numero_dos}")
elif opcion == "/":
    print (f"Resultado de la división = {numero_uno/numero_dos}")
else:
    print ("El signo ingresado no es valido")
    