"""
#Herencia
class Vehiculo:
    
    def mover(self):
        print("El vehículo se está moviendo")
    
class Carro(Vehiculo):
    pass

def main ():
    vehiculo1 = Vehiculo()
    carro1 = Carro()
    
    print("Vehiculo")
    vehiculo1.mover()
    
    print("Carro que hereda de la superclase Vehiculo")
    carro1.mover()
    
if __name__ == "__main__":
    main()

"""
"""
#Herencia con sobrescritura de metodo
class Vehiculo:
    def mover (self):
        print ("El vehículo se está moviendo")

class Carro(Vehiculo):
    def mover(self):
        print("El carro rueda por la calle")
        
def main():
    vehiculo2 = Vehiculo()
    carro2 = Carro()
    
    print("Vehículo")
    vehiculo2.mover()
    
    print("El carro sobre escrbio el método (def)")
    carro2.mover()
    
if __name__ == "__main__":
    main()
    
"""

"""
#Polimorfismo
class Vehiculo:
    def mover (self):
        print ("El vehículo se está moviendo")

class Carro(Vehiculo):
    def mover(self):
        print("El carro rueda por la calle")
        
class Avion(Vehiculo):
    def mover(self):
        print("El avión está volando sobre la ciudad")

def main():
    vehiculo3 = Vehiculo()
    carro3 = Carro()
    avion3 = Avion()
    
    print("Vehículo")
    vehiculo3.mover()
    
    print("Carro")
    carro3.mover()
    
    print("Avión")
    avion3.mover()
    
if __name__ == "__main__":
    main()
"""
"""
#Super
class Padre():
    def __init__(self, mensaje):
        self.mensaje = mensaje
        
class Hijo(Padre):
    def __init__(self, mensaje, nombre):
        super().__init__(mensaje)
        self.nombre = nombre
        
def main():
    
    objeto1 = Hijo("Hola desde la clase hijo", "Kevin Vargas")
    print(objeto1.mensaje)
    print(objeto1.nombre)
    
if __name__ == "__main__":
    main()
"""    
"""
class Empleado():
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento
        
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Salario: {self.salario}")
        print(f"Departamento: {self.departamento}")
        
        
def main():
    gerente = Gerente("Kevin", 90000, "TIC")
    gerente.mostrar_info()
    
if __name__ == "__main__":
    main()
"""
"""
class Empleado():
    def __init__(self, nombre: str):
        self.nombre = nombre
    
    def trabajar(self):
        print(f"{self.nombre} está realizando una tarea general")
        
class Gerente(Empleado):
    def trabajar(self):
        print(f"{self.nombre} está coordinando a su equipo de trabajo")
        
class Desarrollador(Empleado):
    def trabajar(self):
        print(f"{self.nombre} esta desarrollando software")
        
def main():
    empleados = [Gerente("Maryam"), Desarrollador("Juan Esteban"), Empleado("Kevin")]
    
    print("POLIMORFISMO")
    
    for empleado in empleados:
        empleado.trabajar()

if __name__ == "__main__":
    main()
"""

class Animal():
    def __init__(self, nombre):
        self.nombre = nombre

    
class Gato(Animal):
    def __init__(self, nombre, vidas):
        super().__init__(nombre)
        self.vidas = vidas
        
class Perro(Animal):
    def __init__(self, nombre, trucos):
        super().__init__(nombre)
        self.trucos = trucos
        
def main():
    gato = Gato("Michi", "7 vidas")
    perro = Perro("Max","Rodar, Perseguirse la cola, Hacerse el muertito")
    
    print(f"{gato.nombre} tiene {gato.vidas}")
    
    print(f"{perro.nombre} sabe {perro.trucos}")

if __name__ == "__main__":
    main()
