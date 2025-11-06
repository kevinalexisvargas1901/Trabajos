contador = 1

while contador <=5:
    print("Contador", contador)
    contador += 1

print("Fin del ciclo")

palabra = ""

while palabra != "salir":
    palabra = input("Escribe una plabra: ")
    print(f"Escribiste la palabra: {palabra}")
    
print("Programa Finalizado")