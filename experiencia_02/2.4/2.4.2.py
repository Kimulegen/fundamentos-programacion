# EJERCICIO 1
n_bultos = int(input("Ingrese la cantidad de bultos"))
livianos = 0
normales = 0
total_liviano = 0
total_normal = 0


for i in n_bultos:
    peso = int(input(f"Ingresa el peso del bulto {i} (en kg)"))
    
    if 1 <= peso <= 5:
        livianos += 1
        total_liviano += 1000
    elif 6 <= peso <= 10:
        normales += 1
        total_normal +=2000
    else:
        print("Bulto demasiado pesado, favor ingrese otro")   
    

print(f"{livianos} bulto(s) liviano(s) ${total_liviano}")
print(f"{normales} bulto(s) normal(es) ${total_normal}")
print(f"Valor total a pagar: ${total_liviano + total_normal}")
    
# EJERCICIO 2
n_bultos = int(input("Ingrese la cantidad de bultos"))
livianos = 0
normales = 0
total_liviano = 0
total_normal = 0
i = 1

while i <= n_bultos:
    peso = int(input(f"Ingresa el peso del bulto {i} (en kg)"))
    
    if 1 <= peso <= 5:
        livianos += 1
        total_liviano += 1000
    elif 6 <= peso <= 10:
        normales += 1
        total_normal +=2000
    else:
        print("Bulto demasiado pesado, favor ingrese otro") 

    i += 1
  
print(f"{livianos} bulto(s) liviano(s) ${total_liviano}")
print(f"{normales} bulto(s) normal(es) ${total_normal}")
print(f"Valor total a pagar: ${total_liviano + total_normal}")

# EJERCICIO 3
try: 
    numerador = float(input("Ingrese el numerador"))
    denominador = float(input("Ingrese el denominador"))

    if denominador == 0:
        raise ValueError("¡Error! El divisor no puede ser cero")
    
    resultado = numerador / denominador

    print(f"El resultado de la división es: {resultado}")

except ValueError as ve:
    print(f"Error: {ve}")
except ZeroDivisionError:
    print("¡Error! No se puede dividir por cero")
finally:
    print("Fin del programa")