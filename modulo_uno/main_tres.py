"""
while True:
    entrada = input("Ingrese la hora (0-23): ")
    
    if entrada.isdigit():
        hora = int(entrada)
        if hora >= 0 and hora <=23:
            break
    else:
        print("Error: la hora debe estar entre 0 y 23")

if hora >=0 and hora <=12: 
    print("Estamos en el horario de la mañana")
elif hora >=12 and hora <=18:
    print("Estamos en el horario de la tarde")
elif hora >= 18 and hora <=23:
    print("Estamos en horario de la noche")
    

compra = float(input("Ingrese el valor de la compra: "))

if compra >= 50000:
    descuento = 0.20
elif compra >= 20000 and compra < 50000:
    descuento = 0.10
else:
    descuento = 0.0

valor_final = compra * (1 - descuento)
(1 - descuento)
print(f"El descuento aplicado es de {descuento*100:.0f}%")
print(f"Total a pagar: {valor_final:,.2f}")


while True:
    try:
        sistolica = int(input("Ingrese la presión sistólica: "))
        diastolica = int(input ("Ingrese la presión diastólica"))
        
        if sistolica <= 0 or diastolica <= 0:
            print("Los valores deben ser positivos. Intente de nuevo. \n")
            continue
        if sistolica > 300 or diastolica > 200:
            print("Los valores se encuentran fuera de un rango fisiológico \n")
            continue
        break

    except ValueError as e:
        print("Entrada no valida. Ingrese solo números enteros")
    
    if sistolica < 90 or diastolica < 60:
         print("Tiene baja")
    elif sistolica <=120 and diastolica <= 80:
        print("Presión normal")
    else:
        print("A correr al hospital")
        

while True: 
    try:
        velocidad = float(input("Ingrese la velocidad del vehículo (km/h): "))
        
        if velocidad < 0:
            print("La velocidad no puede ser negativa. Intente de nuevo \n")
            continue
        if velocidad > 200:
            print ("La velocidad esta fuera de tango razonable. Intente de nuevo \n")
            continue
        break
    except ValueError:
        print("Entrad no Validad. Intente de nuevo")
        
    if velocidad == 0:
        print("El vehículo está detenido")
    elif velocidad > 0 and velocidad <= 60:
        print("La velocidad es normal")
    elif velocidad > 60 and velocidad <= 30:
        print("La velocidad es rápida")
    else:
        print("El vehículo va a exceso de velocidad")
"""
    
while True: 
    try:
        salario = float(input("Ingrese su salario: "))
        
        if salario < 0:
            print("El salario no puede ser un valor negativo. Intente de nuevo \n")
            continue
        break
    except ValueError:
        print("Entrada no Validad. Intente de nuevo")
        
if salario <= 2000000:
        impuesto = 0
elif salario >= 2000000 and salario <= 5000000:
        impuesto = 0.10
elif salario >= 5000000:
        impuesto = 0.20
    
valor_impuesto = salario * (1 -impuesto)
print(f"Su salario mas el impuesto es de: {valor_impuesto:,.2f}")