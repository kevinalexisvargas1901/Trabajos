#Acceso y actualización de diccionarios
"""
usuarios = {
    "u001": {"nombre": "Ana", "correo": "ana@mail.com", "roles": ["admin"]},
    "u002": {"nombre": "Pedro", "correo": "pedro@mail.com", "roles": ["cliente"]}
}

#Accederal nombre del usuario u001
print("Nombre del u001:", usuarios['u001']['nombre'])

#Agregar un nuevo rol al usuario u002
usuarios['u002']['roles'].append('ventas')
print("Roles actualizados del usuario u002: ", usuarios['u002']['roles'])

#Agregar un nuevo usuario
usuarios['u003']={
    "nombre": "Luisa",
    "correo": "luisa@mail.com",
    "roles": ["soporte", "cliente"]
}
usuarios['u004']={
    "nombre": "Kevin",
    "correo": "kevin@mail.com",
    "roles": ["comprador"]
}

print("\nListado de usuarios registrados:")
for id_usuario, valores_usuario in usuarios.items():
    print(f"{id_usuario} - {valores_usuario}")
    
#Buscar un usuario deacuerdo a su rol
rol = "secretario"
print(f"\nBuscar el rol {rol}")
for id_usuario, valores_usuario in usuarios.items():
    if rol in valores_usuario.get("roles",[]):
        print(f"Usuario: {id_usuario} - Nombre: {valores_usuario['nombre']}")
"""
from typing import Dict, Any

biblioteca: Dict[str, Dict[str, Any]] = {
    "L001": {
        "titulo": "Cien años de soledad",
        "autor": "Gabriel García Márquez",
        "año": 1967,
        "disponible": True
    },
    "L002": {
        "titulo": "1984",
        "autor": "George Orwell",
        "año": 1949,
        "disponible": False
    },
    "L003": {
        "titulo": "Don Quijote de la Mancha",
        "autor": "Miguel de Cervantes",
        "año": 1605,
        "disponible": True
    }
}

DISPONIBLE = "Disponible"
NO_DISPONIBLE = "No disponible"

#Funciones auxiliares
def _obtener_libro(codigo: str) -> Dict[str, Any]:
    if codigo not in biblioteca:
        raise KeyError(f"Libro con código {codigo} no encontrado.")
    return biblioteca[codigo]

def _estado_legible(disponible: bool) -> str:
    return DISPONIBLE if disponible else NO_DISPONIBLE

def mostrar_libro(codigo: str) -> None:
    """Muestra la información detallada de un libro."""
    try:
        libro = _obtener_libro(codigo)
        print(f"\nCódigo: {codigo}")
        print(f"Título: {libro['titulo']}")
        print(f"Autor: {libro['autor']}")
        print(f"Año: {libro['año']}")
        print(f"Estado: {_estado_legible(libro['disponible'])}")
    except KeyError as error:
        print(f"\n{error}")

def cambiar_disponibilidad(codigo: str) -> None:
    """Cambia el estado de disponibilidad de un libro."""
    try:
        libro = _obtener_libro(codigo)
        libro["disponible"] = not libro["disponible"]
        print(
            f"\nEstado actualizado del libro {codigo}: "
            f"{_estado_legible(libro['disponible'])}"
        )
    except KeyError as error:
        print(f"\nNo se pudo cambiar la disponibilidad. {error}")

def main() -> None:
    """Punto de orquestación del sistema de biblioteca."""

    # Pruebas del sistema
    mostrar_libro("L001")
    cambiar_disponibilidad("L001")
    mostrar_libro("L001")
    
    mostrar_libro("L001")
    cambiar_disponibilidad("L001")
    mostrar_libro("L001")

    mostrar_libro("L999")
    cambiar_disponibilidad("L999")


if __name__ == "__main__":
    main()