mi_set = set()

frutas = {"Pera", "Manzana", "Banano"}

# conversión de lista a set
numeros = [1,2,2,3]
conversion = set(numeros)
print(conversion)

frutas.add("Uva")
print(frutas)

frutas.update(["kiwi", "mango"])
print(frutas)

frutas.discard("pera")#Aqui no da error al intentar borrarlo (si ya ha sido eliminado)
print(frutas)

frutas.remove("pera")#Aqui si da error al intentar borrarlo (si ya ha sido eliminado)

ordenado = sorted(frutas)
print(ordenado)

frutas.clear()

#Operaciones con set
#Union
#Intesección
#Diferencia
#Diferencia simétrica

a = {1, 2, 3}
b = {3, 4 , 5}

print(a | b)

print(a & b)

print(a - b)

print(a ^ b)

#validación de elementos con set
usuarios = {"Maryam", "Pablo", "Ignacio"}
print("Maryan" in usuarios) #True or False
print("Luis" in usuarios) #True or False
