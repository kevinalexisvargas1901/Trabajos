"""
def agregar_cliente(Lista_clientes, nombre):
    if isinstance(nombre, str) and 2 <= len(nombre) <= 50:
        Lista_clientes.append(nombre.title())
        print("Cliente agregado")
    else:
        print("Nombre inválido")
        
def mostrar_clientes(Lista_clientes):
    for cliente in Lista_clientes:
        print(cliente)
        
def modificar_cliente(Lista_clientes, indice, nuevo_nombre):
    if not (isinstance(nuevo_nombre, str)) and 2 <= len(nuevo_nombre) <= 50:
        print ("Nombre inválido")
        return
    if 0 <= indice < len(Lista_clientes):
        Lista_clientes[indice] = nuevo_nombre.title()
        print("Cliente modificado")
    else:
        print("Indice fuera del rango")
        
def eliminar_cliente(Lista_clientes, indice):
    if 0 <= indice < len(Lista_clientes):
        eliminado = Lista_clientes.pop(indice)
        print(f"Cliente eliminado: {eliminado}")
    else:
        print("Indice fuera del rango")

def main():
    clientes= ["Andrés", "Cesar", "Melany"]
    print("Clientes Actuales\n")
    mostrar_clientes(clientes)
    
    agregar_cliente(clientes, "Juan")
    modificar_cliente(clientes, 0, "Rigel")
    eliminar_cliente(clientes, 2)
    
    mostrar_clientes(clientes)
    
if __name__ == "__main__":
    main()
"""

# Ejercicio empresarial real: Gestión de inventario en una ferretería. Simular un sistema básico de control de inventario donde se pueda:

# Agregar nuevos productos (`.append()`)
# Insertar productos en una posición específica (`.insert()`)#
# Eliminar productos agotados (`.remove()` / `.pop()`)
# Ordenar productos alfabéticamente ó por precio (`.sort()`)
# Invertir el orden de presentación de productos (`.reverse()`)

# Requisitos del sistema de información:
# 1. Lista de productos con nombre y precio.
# 2. Operaciones de mantenimiento de la lista (usando los métodos mencionados).
# 3. Validación de entradas.

def mostrar_inventario(productos):
    print("\nInventario actualizado")
    if not productos:
        print("No hay inventario")
        return
    for i, producto in enumerate(productos, start=1):
        print(f"{i}. {producto['nombre']} - ${producto['precio']:.2f}")

def agregar_producto(productos, nombre, precio):
    if isinstance(nombre, str) and nombre.strip() and isinstance(precio, (int, float)) and precio > 0:
        productos.append({"nombre": nombre.title(), "precio": precio})
        print("Producto agregado con éxito")
    else:
        print("Datos invalidos")

def insertar_producto(productos, indice, nombre, precio):
    if 0 <= indice <= len(productos) and isinstance(nombre, str) and isinstance(precio, (int, float)) and precio > 0:
        productos.insert(indice, {"nombre": nombre.title(), "precio": precio})
        print(f"Producto insertado en la pocisión {indice + 1}.")
    else:
        print("Por favor, revise los datos e intente de nuevo")

def eliminar_producto(productos, nombre):
    for producto in productos:
        if producto["nombre"].lower() == nombre.lower():
            productos.remove(producto)
            print("Producto eliminado con éxito")
            return
    print("Producto no encontrado")

def eliminar_ultimo(productos):
    if productos:
        eliminado = productos.pop()
        print(f"El último elemento de la lista fue eliminado -> {eliminado['nombre']}")
    else:
        print("Inventario vacio")

def ordenar_por_nombre(productos):
    productos.sort(key=lambda x: x["nombre"])
    print("Productos ordenado de forma alfabética")

def ordenar_por_precio(productos, descendente=False):
    productos.sort(key=lambda x: x["precio"], reverse=descendente)
    orden = "descendente" if descendente else "ascendente"
    print(f"Productos ordenados por precio de forma ({orden}).")

def invertir_inventario(productos):
    productos.reverse()
    print("Inventario invertido")

def main():
    inventario = [
        {"nombre": "Taladro", "precio": 150.00},
        {"nombre": "Martillo", "precio": 40.00},
        {"nombre": "Destornillador", "precio": 15.00}
    ]
    
    mostrar_inventario(inventario)
    agregar_producto(inventario, "Machete", 50)
    mostrar_inventario(inventario)
    insertar_producto(inventario, 2, "Broca", 10)
    mostrar_inventario(inventario)
    eliminar_producto(inventario, "Taladro")
    mostrar_inventario(inventario)
    eliminar_ultimo(inventario)
    mostrar_inventario(inventario)
    ordenar_por_nombre(inventario)
    mostrar_inventario(inventario)
    ordenar_por_precio(inventario)
    mostrar_inventario(inventario)
    invertir_inventario(inventario)
    mostrar_inventario(inventario)
    
        
if __name__ == "__main__":
    main()
    