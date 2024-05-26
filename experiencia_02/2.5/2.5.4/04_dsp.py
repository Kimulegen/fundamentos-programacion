import time

while True:
    espacios = ""
    linea = "*"
    for i in range(11):
        print(linea)
        espacios += " "
        linea = espacios + linea
        time.sleep(0.05)
    
    for i in range(14):
        print(linea)
        espacios = " "
        linea = linea[i:]
        time.sleep(0.05)
    
    linea = "*"
    espacio = " "
    for i in range(22):
        linea += " *"
        espacio += "  "
    print(linea)

    espacio += "*"
    for i in range(14):
        print(espacio)
        time.sleep(0.05)
    print(linea)