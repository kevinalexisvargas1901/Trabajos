"""
from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre: str) -> None:
        self._nombre = None
        self.nombre = nombre
        
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor: str) -> None:
        if isinstance(valor, str) and valor.strip():
            self._nombre = valor.strip()
        else:
            raise ValueError("El nombre debe ser un texto no vacío")
        
    @abstractmethod
    def trabajar(self) -> None:
        pass
    
class Gerente(Empleado):
    def trabajar(self):
        print(f"{self.nombre} está gestionando estrategias empresariales.")
        
class Desarrollador(Empleado):
    def trabajar(self):
        print(f"{self.nombre} esta codificando un software.")

def ejecutar_tarea (empleado: Empleado) -> None:
    empleado.trabajar()
    
def main() -> None:
    empleado1 = Gerente("Kevin Vargas")
    empleado2 = Desarrollador("Carlos Palacio")
    
    ejecutar_tarea(empleado1)
    ejecutar_tarea(empleado2)
    
    empleado2.nombre = "Fernando Restrepo"
    print(f"El nombre nuevo del desarrollador es: {empleado2.nombre}")

if __name__ == "__main__":
    main()
"""
#Interfaces / clases abc
#En las interfaces se deben de definir todos los metodos
#solo comportamientos

from abc import ABC, abstractmethod

#interfaz para generar reportes
class GenerarReporte(ABC):
    
    @abstractmethod
    def generar_reporte(self) -> None:
        pass
    
class SistemaPago(ABC):
    def __init__(self, monto: float) -> None:
        self.monto = monto
        
    @abstractmethod
    def procesar_pago(self) -> None:
        pass
    
class PagoCriptomoneta(SistemaPago):
    def procesar_pago(self):
        print(f"Procesando el pago con cryptomonetas por ${self.monto:,.2f}")
        
class PagoBancario(SistemaPago, GenerarReporte):
    def procesar_pago(self) -> None:
        print(f"Procesando transferencia bancaria por un monto de ${self.monto:,.2f}")
        
    def generar_reporte(self) -> None:
        print("Reporte: Pago realizado mediante sistema bancario")

def ejecutar_pago(pago:SistemaPago) -> None:
    pago.procesar_pago()
    
def main() -> None:
    pago1 = PagoBancario(12.3123123)
    pago2 = PagoCriptomoneta(23.43434)
    
    ejecutar_pago(pago1)
    pago1.generar_reporte()
    
    ejecutar_pago(pago2)

if __name__ == "__main__":
    main()
        