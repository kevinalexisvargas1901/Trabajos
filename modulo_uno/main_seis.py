#lista
estudiantes = []

def registrar_estudiantes():
    print("\n---Registrar estudiante---")
    nombre = input ("Nombre: ").strip().title()
    edad = int(input("Edad: "))
    nota = float(input("Nota (0 - 5): "))
    estudiante = {"nombre": nombre, "edad": edad, "nota": nota}
    estudiantes.append(estudiante)
    print("Estudiante registrado con éxito")
    
def mostrar_estudiante():
    print("\n---Lista de estudiantes---")
    if not estudiantes:
        print("No hay estudiantes registrados")
    else:
        for i, e in enumerate(estudiantes, 1):
            print(f"{i}. {e['nombre']} - {e['edad']} años - Nota:{e['nota']}")

def buscar_estudiante():
    print ("\n---Buscar estudiante por nombre---")
    nombre = input("Ingrese el nombre a buscar: ").strip().lower()
    
    encontrados = [e for e in estudiantes if nombre in e["nombre"].lower()]
    
    if encontrados:
        for e in encontrados:
            print(f"{e['nombre']} - {e['edad']} años - Nota:{e['nota']}")         
    else:
        print ("No se encontró ningún estudiante registrado.")
        
def calcular_promedio():
    print("\n---Promedio general---")
    if not estudiantes:
        print ("No hay estudiantes registrados.")
        return
    notas = [e ["nota"] for e in estudiantes]
    promedio = sum(notas) / len(notas)
    print(f"Promedio general: {promedio:.1f}")
    
def menu():
    while True:
        print("\n*** MENU PRINCIPAL ***")
        print("1. Registrar estudiantes.")
        print("2. Mostrar todos los registros.")
        print("3. Buscar estudiante por nombre.")
        print("4. Calcular promedio general.")
        print("5. Salir.")
        
        opcion = input("Elija una opción (1-5): ")
        
        if opcion == "1" :
            registrar_estudiantes()
        elif opcion == "2":
            mostrar_estudiante()
        elif opcion == "3":
            buscar_estudiante()
        elif opcion == "4":
            calcular_promedio()
        elif opcion == "5":
            print("Hasta luego")
            break
        else:
            print ("Opcion inválida")
            
def main():
    menu()

if __name__ == "__main__":
    main()