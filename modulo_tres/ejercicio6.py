"""
# Usar set para validar si un usuario tiene acceso a un sistema.

from typing import Set, List, Tuple

def _obtener_usuarios_con_acceso(
    usuarios_autorizados: Set[str],
    usuarios_intentando: Set[str]
)-> Set[str]:
    return {u for u in usuarios_intentando if u in usuarios_autorizados}

def _obtener_usuario_sin_acceso(
    usuarios_autorizados: Set[str],
    usuarios_intentando: Set[str]
)-> Set[str]:
    return { u for u in usuarios_intentando if u not in usuarios_autorizados }

def validar_acceso(
    usuarios_autorizados: Set[str],
    usuarios_intentando: Set[str]
)-> Tuple[Set[str], Set [str]]:
    
    autorizados = set(usuarios_autorizados)
    intentando = set (usuarios_intentando)
    
    acceso = _obtener_usuarios_con_acceso(autorizados, intentando)
    no_acceso = _obtener_usuario_sin_acceso(autorizados, intentando)
    
    return acceso, no_acceso

def main()-> None:
    autorizados = {"Alexis", "Julian", "Pablo"}
    intentando = {"Ignacio", "Jerónimo", "Anobis", "Julian", "Diego", "Pablo"}
    
    acceso, no_acceso = validar_acceso(autorizados, intentando)
    
    print(f"Con acceso: {acceso}")
    print("Sin acceso: ", no_acceso)
    
if __name__ == "__main__":
    main()
"""

def operaciones_productos(tienda_a: set, tienda_b: set):
 
    union = tienda_a | tienda_b
    interseccion = tienda_a & tienda_b
    diferencia = tienda_a - tienda_b

    return union, interseccion, diferencia


def main():
 
    a = {"Laptop", "Mouse", "Teclado"}
    b = {"Mouse", "Pantalla", "Laptop"}

    union, interseccion, diferencia = operaciones_productos(a, b)

    print("Unión:", union)
    print("Intersección:", interseccion)
    print("Diferencia:", diferencia)

if __name__ == "__main__":
    main()


