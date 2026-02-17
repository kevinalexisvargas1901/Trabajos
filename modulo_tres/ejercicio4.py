#Proyecto Ferretería (Diccionarios)

import os
import sys

inventario = {
    
    "001": {"nombre": "Martillo0", "cantidad":50, "precio": 15.99},
    "002":{"nombre": "Destornillador", "cantidad":80, "precio": 7.49},
    "003":{"nombre": "Taladro", "cantidad":20, "precio": 89.99},
    "004":{"nombre": "Sierra", "cantidad":15, "precio": 129.99}
    
}

factura_actual = []

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def mostrar_encabezado_tabla():
    print(f"{'Código':<6}{'ID':<20}{'NOMBRE':<10}{'STOCK':<8}")
    print("-" * 48)
    
def buscar_producto():
    print("\n---BUSCAR POR NOMBRE")
    termino = input("Ingrese el nombre o parte del nombre a buscar: ").strip().lower()
    
    encontrados = False
    print ("\n Resultados de búsqueda:")
    mostrar_encabezado_tabla()
    
    for id_prod, datos in inventario.items():
        if termino in datos["nombre"].lower():
            print(f"{id_prod: <6}{datos['nombre']:<20} ${datos['precio']:<9.2f}")
            encontrados = True
    if not encontrados:
        print("No se encontraron productos con ese nombre")
    print("-" * 48)

def mostrar_inventario():
    print("\n--- INVENTARIO COMPLETO ---")
    if not inventario:
        print("El inventario está vacío")
        return
    else:
        mostrar_encabezado_tabla
        for id_prod, datos in inventario.items():
            print(f"{id_prod: <6}{datos['nombre']:<20} ${datos['precio']:<9.2f}")
    print("-" * 48)
    
def agregar_nuevo_producto():
    print("\n--- REGISTRAR NUEVO PRODUCTO ---")
    id_prod = input("Ingrese un ID único: ").strip()
    
    if id_prod in inventario:
        print("Error: El ID ya existe en el inventario")
    else:
        nombre = input("Ingrese el nombre del producto").strip()
        try:
            precio = float(input("precion unitario: ").strip())
            stock = int(input("stock inicial: ").strip())
            
            inventario[id_prod] = {
                "nombre": nombre,
                "precio": precio,
                "stock": stock
            }
            print(f"Producto {nombre} agregado exitosamente")
            
        except ValueError:
            print("Error: Precio y Stock deben ser números válidos")