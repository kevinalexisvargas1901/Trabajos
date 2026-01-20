from dataclasses import dataclass

@dataclass
class Libro:
    _titulo: str
    _autor: str
    _isbn: str
    _precio: float
    
    @property
    def titulo(self) -> str:
        return self._titulo
    
    @titulo.setter
    def titulo (self, valor: str) -> None:
        if isinstance(valor, str) and valor.strip():
            self._titulo = valor
        else:
            raise ValueError("El titulo debe ser un texto válido, no vacío")
        
    @property
    def autor(self) -> str:
        return self._autor
    
    @autor.setter
    def autor(self, valor: str) -> None:
        if isinstance(valor, str) and valor.strip():
            self._autor = valor
        else:
            raise ValueError("El autor debe ser un texto válido")
    
    @property
    def isbn(self) -> str:
        return self._isbn
    
    @isbn.setter
    def isbn(self, valor:str) -> None:
        if isinstance(valor, str) and valor.strip():
            self._isbn= valor
        else:
            raise ValueError("El isbn debe ser un texto válido")
    
    @property
    def precio (self) -> float:
        return self._precio
    
    @precio.setter
    def precio(self, valor: float) -> None:
        if isinstance ( valor, float) and valor > 0:
            self._precio = valor
        else:
            raise ValueError ("El precio debe ser un numero entero o decimal")
        
    
    def __repr__(self) -> str:
        return(
            f"Libro(titulo='{self._titulo}', autor='{self._autor}',"
            f"\nISBN='{self._isbn}', precio ='{self._precio}')"
            )
        
def main() -> None:
    libro = Libro("Cien años de soledad", "Marquez", "123455432", 50000.00 )
    
    print ("\n *** Informacion del libro ***")
    
    libro.precio= 18000.00
    libro.titulo="Cabañas del amor"
    
    print("*** Datos actualizados ***")
    print(libro)
    
    print("<<< Programa finalizado >>>")
    
if __name__ == "__main__":
    main()

