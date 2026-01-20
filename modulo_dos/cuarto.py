class Empleado:
    def __init__(self, nombre: str):
        if not Empleado.validar_nombre(nombre):
            raise ValueError("El nombre de ser valido")
        self.nombre = nombre
        
    def trabajar(self) -> None:
        print(f"{self.nombre} está realizando tareas generadas")
        
    @staticmethod
    def validar_nombre(nombre: str) -> bool:
        return isinstance(nombre, str) and nombre.strip() !=""
    
class Gerente(Empleado):
    def trabajar(self):
        print(f"{self.nombre} está coordinando los proyectos a su cargo")
        
    def comision(self):
        pass
class Desarrollador(Empleado):
    def trabajar(self):
        print(f"{self.nombre} esta codificando un backend en Python")
        
def ejecutar_tarea(empleado: Empleado) -> None:
    empleado.trabajar()

def main() -> None:
    print("\n¿Es válido introducir Gilberto?", Empleado.validar_nombre("Gilberto"))
    print("\n¿Es válido este nombre?", Empleado.validar_nombre(""))
    print("\n¿Es válido introducir 5555?", Empleado.validar_nombre("5555"))
    print("\n¿Es válido introducir 222?", Empleado.validar_nombre(2222))
    
    empleado1 = Gerente("\nMaryam")
    empleado2 = Desarrollador("Juan Ignacio")
    
    ejecutar_tarea(empleado1)
    ejecutar_tarea(empleado2)
    
if __name__ == "__main__":
    main()