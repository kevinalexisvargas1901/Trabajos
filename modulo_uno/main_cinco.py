def saludar():
    print("Holaaa parce...")
    
saludar()

def saludo():
    return "Hola parce"

print(saludo())

#Funciones con parametro
def saludotres(nombre):
    print(f"Como estas {nombre}")
    
saludotres("Kevin")

def suma(numero1:int, numero2:int) -> int:
    resultado = numero1 + numero2
    print (f"El resultado de la suma de {numero1} + {numero2} es igual a {resultado}")
    
suma(5,5)

#Funciones con parametros ocn valores por defecto
def presentar(nombre: str, carrera: str ="Ingeniería") -> str:
    print (f"Estudiante: {nombre} | Carrera: {carrera}")

presentar("Camilo")
presentar("Maryam", "Medicina")

#Funciones con efecto colateral
estudiantes = []

def agregar_estudiante(nombre: str):
    estudiantes.append(nombre)

agregar_estudiante("Gilberto")
print(estudiantes)