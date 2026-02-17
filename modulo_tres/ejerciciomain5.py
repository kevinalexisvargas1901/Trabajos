""" 
#Eliminar duplicados de una lista

from typing import List

def eliminar_duplicados(numeros: List[int]) -> List[int]:
    
    if not isinstance(numeros, list):
        raise TypeError("Se esperaba una LISTA de números")
    
    if not all(isinstance(n, int) for n in numeros):
        raise ValueError("Todos los elementos dentro de la lista deben ser números enteros")
    
    return sorted(set(numeros))

def main() -> None:
    numeros = [1, 2 ,5 , 8, 7, 6, 4, 5, 1, 9, 7]
    
    print("Lista Original: ", numeros)
    
    try:
        resultado = eliminar_duplicados(numeros)
        print("Sin duplicados: ", resultado)
        
    except (TypeError, ValueError) as error:
        print(f"Error: {error}")
        
if __name__ == "__main__":
    main()  
"""
"""
productos = ["pan", "leche", "huevos", "pan", "arroz", "leche", "pan"]

conversion = set(productos)
print(conversion)

cantidad = len(conversion)
print(f"Hay {cantidad} productos diferentes")
"""
"""
usuarios_autorizados = {"ana", "carlos", "maria", "pedro"}

nombre = input(str("Ingrese el nombre: ")).lower().strip()
if nombre in usuarios_autorizados:
    print("Usuario autorizado, puede ingresar")
else:
    print("Este usuario no está autorizado en el sistema, no puede ingresar")
"""
"""
online = {"Juan", "Ana", "Pedro", "Lucia"}
tienda = {"Ana", "Pedro"}

print(f"Los clientes exclusivos online son: {online - tienda}")
"""

sucursal_1 = {"Carlos", "Maria", "Andres"}
sucursal_2 = {"Maria", "Luisa", "Carlos", "Elena"}

print(f"Base de clientes: {sucursal_1 | sucursal_2}")