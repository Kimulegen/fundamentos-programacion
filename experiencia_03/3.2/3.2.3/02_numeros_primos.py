def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


rango_inferior = int(input("Ingrese el rango inferior: "))
rango_superior = int(input("Ingrese el rango superior: "))
primes = set()

for i in range(rango_inferior,rango_superior + 1):
    if i == 1: 
        continue
    if is_prime(i):
        primes.add(i)

print(primes)

# ALGO EJERCICIO
numeros_primos = {num for num in range(rango_inferior, rango_superior + 1) if num > 1 and all(num % i !=0 for i in range(2, int(num**0.5) + 1))}
