```python
user = input("Ingrese su user")
pwd = input("Ingrese su pass")

if user == "duoc" and pwd == "123duoc":
    valorDev = int(input("Bienvenido, ingrese el valor a devolver: "))
    if valorDev > 100000:
        print("Se dará la máxima urgencia a su devolución de dinero")
    else:
        print("El caso ha quedado registrado, le informaremos lo antes posible")
else:
    print("Error en contraseña")
```

#### Qué mensaje nos imprimirá el sistema, si nos devuelve una devolución de dinero de $120.000, e ingresamos el user "duoc123" y el pass "123duoc"?
R: Error en contraseña