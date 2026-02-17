#algun ejemplo de diccionario (dict)
persona = {
    "nombre": "Luis", 
    "edad":50, 
    "residencia": "Colombia"
}

cliente = dict(
    nombre = "Luis",
    telefono = "3134230579"
)

#Imprimir un elemento
print(cliente["nombre"])
print(cliente.get("telefono"))

paciente = {"nombre": "Paco", "especie": "Loro", "edad": 5, "vacunado": True}

#Uso de método .keys()
print("Claves registradas en el diccionario")
for clave in paciente.keys():
    print(f"Claves disponibles: {clave}")
    
print("Valores disponibles en el diccionario")
for valor in paciente.values():
    print(f"Valores disponibles: {valor}")
    
print("\nRegistro completo de pacientes registrados\n")
for clave, valor in paciente.items():
    print(f"Clave: {clave} - Valor: {valor}")
    
#actualizar un registro de diccionario
print("\nActualizacion del registro del paciente\n")
paciente.update({"especie": "canino", "edad": 5, "vacunado": False})
for clave, valor in paciente.items():
    print(f"Clave: {clave} - Valor: {valor}")  

dato_eliminado = paciente.pop("especie", None) 
print("\nDatos actualizados despues de borrar un dato")
for clave, valor in paciente.items():
    print(f"Clave: {clave} - Valor: {valor}")