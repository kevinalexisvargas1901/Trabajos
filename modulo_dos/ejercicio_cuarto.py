"""
from abc import ABC, abstractmethod

class Figura(ABC):
    
    @abstractmethod
    def calcular_area(self):
        pass
    
class Circulo(Figura):
    def __init__(self, radio: float):
        self.radio = radio
        
    def calcular_area(self):
        area = 3.1416 * (self.radio ** 2)
        return area
    
    def calcular_radio(self):
        pass
    
    def calcular_perímetro(self):
        pass

def main():
    figura1 = Circulo(5.0) 
    print(f"El área del circulo es {figura1.calcular_area():,.2f}")
    
if __name__ == "__main__":
    main()
"""

from abc import ABC, abstractmethod

class Estudiante(ABC):
    
    def __init__(self, nombre, id):
        self.nombre = nombre
        self.id = id
    
    @abstractmethod
    def matricular(self, curso):
        pass
    
    @abstractmethod
    def pagar_matricula(self, monto):
        pass
        
class Pregrado(Estudiante):
    def __init__(self, nombre, id, carrera):
        super().__init__(nombre, id)
        self.carrera = carrera

    def matricular(self, curso):
        print(f"\nNombre: {self.nombre} \nID: {self.id} \nSe matriculó en {curso} de la carrera {self.carrera}")

    def pagar_matricula(self, monto):
        print(f"El estudiante de pregrado {self.nombre} ha realizado un pago de ${monto}")

class Postgrado(Estudiante):
    def __init__(self, nombre, id, postgrado):
        super().__init__(nombre, id)
        self.postgrado = postgrado

    def matricular(self, curso):
        print(f"\nNombre: {self.nombre} \nID: {self.id} \nSe matriculó en {curso} del postgrado {self.postgrado} ")
        
    def pagar_matricula(self, monto):
        print(f"El estudiante de postgrado {self.nombre} ha realizado un pago de ${monto}")

class Escolar(Estudiante):
    def __init__(self, nombre, id, grado):
        super().__init__(nombre, id)
        self.grado = grado

    def matricular(self, curso):
        print(f"\nNombre: {self.nombre} \nID: {self.id} \nEl acudiente matriculó al estudiante para el curso de {curso} del grado {self.grado}")

    def pagar_matricula(self, monto):
        print(f"El acudiente del estudiante de escolar {self.nombre} ha realizado un pago de ${monto}")
        
def main():
    pregrado = Pregrado("Carlos", "121212", "Ingeniería Civil")
    postgrado = Postgrado("Maria", "123321", "Redes")
    escolar = Escolar("Ana", "12345", "Quinto")
    
    pregrado.matricular("Introducción a la Ing Civil")
    pregrado.pagar_matricula(15000000)
    
    postgrado.matricular("Redes 1")
    postgrado.pagar_matricula(1800000)
    
    escolar.matricular("Artística")
    escolar.pagar_matricula(1200000)
    
if __name__ == "__main__":
    main()
