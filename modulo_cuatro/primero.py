"""
f = open("datos.txt", "r")
file1 = open("datos.txt", "w")
file2 = open("datos.txt", "a")
file3 = open("datos.txt", "r+")

with open("datos.txt", "r", encoding="utf-8") as f:
    contenido = f.read()
    
"""
#Metodo de lectura .read()

with open("letras.txt", "w", encoding="utf-8") as f:
    f.write("A\n")
    f.write("B\n")
    f.write("C\n")

with open("letras.txt", "r", encoding="utf-8") as f:
    print(f.read())

#Método .readline() imprimer una lista de contenidos en el archivo

with open("letras.txt", "r", encoding="utf-8") as f:
    print(f.readline())

with open("letras.txt", "r", encoding="utf-8") as f:
    print(f.readlines())
    
#Convención
#Nombre|apellido|edad
#Luis|molero|50

#Arquitectura minima p/manejo de archivos
#Presentación -> Integracion con el usuario
#Servicio -> modelo/reglas del negocio
#Infraestructura -> archivos físicos
#modelo/esquem -> datos

#Super Software
"""
FileManager (infraestructura segura)
Modelo Task (serialización)
Repository (persistencia desacoplada)
Service (reglas de negocio + validación)
main (interfaz consola)
ejercicio práctico sistema de tareas
"""

#ToDo List

"""
PEP8	       | nombres, longitud, imports
DRY	           | no repetir lógica de archivo
KISS	       | funciones pequeñas
SRP	           | cada función hace una sola cosa
Fail           | Fast	validar antes de guardar
Defensive      | Programming	proteger el archivo
Idempotencia   | leer no modifica estado
Encapsulación  | no acceder directo al archivo
Tipado         | fuerte	typing obligatorio
"""
