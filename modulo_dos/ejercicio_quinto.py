from abc import ABC, abstractmethod

class Movible(ABC):
    
    @abstractmethod
    def mover(self) -> None:
        pass

class Animal(ABC):
    
    def __init__(self, nombre:str):
        self._nombre = str = ""
        self.nombre = nombre
        
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre (self, valor: str) -> None:
        if isinstance(valor, str) and valor.strip():
            self._nombre = valor.strip().title()
        else:
            raise ValueError("El nombre debe ser una cadena de texto válida")
    
    @abstractmethod
    def sonido(self) -> None:
        pass

class Perro(Animal):
    
    def sonido(self):
        print(f"{self.nombre} el perro hace: ¡Guau Guau!")
    
class Gato(Animal):
    
    def sonido(self):
        print(f"{self.nombre} el gato hace: ¡Miau Miau!")

class Vaca(Animal):
    
    def sonido(self):
        print(f"{self.nombre} la vaca hace: ¡Muuu!")

class Leon(Animal, Movible):
    
    def sonido(self):
        print(f"{self.nombre} el león hace: ¡Grrr Grrr!")
        
    def mover(self):
        print(f"{self.nombre} se ha desplazado por toda la jungla, cuidando su reino")
    
def ejecutar_sonido(animal: Animal):
    animal.sonido()
    
def main() -> None:
    perro = Perro("Max")
    gato = Gato("Michi")
    vaca = Vaca("Rosa")
    leon = Leon("Alex")
    
    ejecutar_sonido(perro)
    ejecutar_sonido(gato)
    ejecutar_sonido(vaca)
    ejecutar_sonido(leon)
    
    leon.mover()

if __name__ == "__main__":
    main()