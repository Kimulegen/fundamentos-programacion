#! Python3
# Generate a set with prime numbers between a certain range


# function that checks if a number is prime
def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# initialize variables
primes = set()

# ask for ranges
rango_inferior = int(input("Ingrese el rango inferior: "))
rango_superior = int(input("Ingrese el rango superior: "))

# create set with prime numbers
for i in range(rango_inferior, rango_superior + 1):
    if i == 1:
        continue
    if is_prime(i):
        primes.add(i)

# show set
print(primes)

# ALTERNATIVE ANSWER
numeros_primos = {
    num
    for num in range(rango_inferior, rango_superior + 1)
    if num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))
}
