#! Python
# Show discount by age

# ask for age
edad = int(input("Ingrese su edad"))

# show discount
if edad > 0 and edad < 18:
    print(f"Edad: {edad}, tiene un descuento de un 50%")
elif edad >= 18 and edad < 30:
    print(f"Edad: {edad}, tiene un descuento de un 20%")
elif edad >= 60:
    print(f"Edad: {edad}, tiene un descuento de un 90%")
else:
    print(f"Edad: {edad}, no aplica descuento")
