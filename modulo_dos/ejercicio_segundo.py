from dataclasses import dataclass

@dataclass
class ProductoIndustrial:
    _nombre: str
    _categoria: str
    _codigo_interno: str
    _precio_unitario: float
    _cantidad_inventario: int
    
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre (self, valor: str) -> None:
        if isinstance(valor, str) and valor.strip():
            self._nombre = valor
        else:
            raise ValueError("El nombre debe ser un texto válido, no vacío")
        
    @property
    def categoria(self) -> str:
        return self._categoria
    
    @categoria.setter
    def categoria(self, valor: str) -> None:
        if isinstance(valor, str) and valor.strip():
            self._categoria = valor
        else:
            raise ValueError("La categoría debe ser un texto válido")
    
    @property
    def codigo_interno(self) -> str:
        return self._codigo_interno
    
    @codigo_interno.setter
    def codigo_interno(self, valor:str) -> None:
        if isinstance(valor, str) and valor.strip():
            self._codigo_interno= valor
        else:
            raise ValueError("El codigo debe ser un texto válido")
    
    @property
    def precio_unitario (self) -> float:
        return self._precio_unitario
    
    @precio_unitario.setter
    def precio_unitario(self, valor: float) -> None:
        if isinstance ( valor, float) and valor > 0:
            self._precio_unitario = valor
        else:
            raise ValueError ("El precio debe ser un numero entero o decimal")
        
    @property
    def cantidad_inventario(self) -> int:
        return self._cantidad_inventario
    
    @cantidad_inventario.setter
    def cantidad_inventario(self, valor: int)-> None:
        if isinstance (valor, int) and valor > 0:
            self._cantidad_inventario = valor
        else:
            raise ValueError("El número ingresado es incorrecto")
    
    
    def __repr__(self) -> str:
        return(
            f"Producto(nombre='{self._nombre}', categoria='{self._categoria}',"
            f"\ncodigo='{self._codigo_interno}', precio ='{self._precio_unitario}', cantidad = '{self._cantidad_inventario}')"
            )
        
def main() -> None:
    producto = ProductoIndustrial("Licuadora", "Electrodoméstico", "123455432", 50000.00, 5)
    
    print ("\n *** Informacion del producto ***")
    print(producto)
    
    producto.precio_unitario= 18000.00
    producto.cantidad_inventario= 7
    
    print("*** Datos actualizados ***")
    print(producto)
    
    print("<<< Programa finalizado >>>")
    
if __name__ == "__main__":
    main()