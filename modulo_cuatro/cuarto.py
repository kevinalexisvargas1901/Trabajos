
try:
    edad = int(input("Ingrese su edad: "))
except ValueError:
    print("Debe ingresar un número")
except TypeError:
    print("Tipo de dato inválido")
except Exception as e:
    print("Ocurrió un error inesperado: ", e)
    
    
try:
    edad = int(input("Ingrese su edad: "))
except ValueError:
    print("Debe ingresar un número")
else:
    print("La ejecución de un resultado positivo (Else)")
finally:
    print("La ejecución finalizó")
    
#Excepsiones globales


class edadInvalidaError(Exception):
    pass

class EdadNegativaError(Exception):
    pass

try:
    entrada = input("Ingrese la edad: ")

    if not entrada.isdigit():
        raise edadInvalidaError("La edad debe ser un número entero")

    edad = int(entrada)

    if edad <= 0:
        raise EdadNegativaError("La edad no puede ser igual a cero o negativa")

except edadInvalidaError as e:
    print(f"Error de formato: {e}")

except EdadNegativaError as e:
    print(f"Error lógico: {e}")

else:
    print(f"La edad {edad} es válida")

finally:
    print("Fin de la ejecución del programa...")
    
    