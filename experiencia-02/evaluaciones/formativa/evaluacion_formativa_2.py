#! python3
# Sushi delivery

import os

PIKACHU_ROLL = 4500
OTAKU_ROLL = 5000
PULPO_ROLL = 5200
ANGUILA_ROLL = 4800

total_compra = n_pikachu = n_otaku = n_pulpo = n_anguila = 0


def print_compra():
    print("Lleva comprado hasta ahora:")
    print(f"Pikachu Roll: {n_pikachu}")
    print(f"Otaku Roll: {n_otaku}")
    print(f"Pulpo Venenoso Roll: {n_pulpo}")
    print(f"Anguila Eléctrica Roll: {n_anguila}")


c1 = 1
while c1 == 1:
    print(" Menú ".center(30, "="))
    print(f"1. Pikachu Roll ${PIKACHU_ROLL}")
    print(f"2. Otaku Roll ${OTAKU_ROLL}")
    print(f"3. Pulpo Venenoso Roll ${PULPO_ROLL}")
    print(f"4. Anguila Eléctrica Roll {ANGUILA_ROLL}")
    print("5. Terminar pedido")

    try:
        print("Elija su opción")
        op = int(input("> "))
        if not (1 <= op <= 5):
            raise ValueError
    except ValueError:
        print("Opción inválida")
        continue

    os.system("cls||clear")
    if op == 1:
        n_pikachu += 1
        total_compra += PIKACHU_ROLL
        print("Usted ha añadido Pikachu Roll a su compra")
        print_compra()
    elif op == 2:
        n_otaku += 1
        total_compra += OTAKU_ROLL
        print("Usted ha añadido Otaku Roll a su compra")
        print_compra()
    elif op == 3:
        n_pulpo += 1
        total_compra += PULPO_ROLL
        print("Usted ha añadido Pulpo Venenoso Roll a su compra")
        print_compra()
    elif op == 4:
        n_anguila += 1
        total_compra += ANGUILA_ROLL
        print("Usted ha añadido Anguila Eléctrica Roll a su compra")
        print_compra()
    elif op == 5:
        desc = 0
        desc = input("¿Posee un código de descuento? (s/n)\n> ")
        if desc == "s":
            c2 = 1
            while c2 == 1:
                codigo = input("Ingrese su código\n> ")
                if codigo == "soyotaku":
                    desc = 0.1
                    total_compra *= 0.9
                    c1 = 0
                    c2 = 0
                else:
                    desc = 0
                    print("código no válido")
                    respuesta = input(
                        "¿Desea reingresar su código? si desea volver al menú presione X (s/n/X)\n> "
                    )
                    if respuesta == "X":
                        c2 = 0
                    elif respuesta == "s":
                        continue
                    else:
                        c2 = 0
                        c1 = 0
        else:
            desc = 0
            break

print("*" * 30)
print(f"TOTAL PRODUCTOS {n_pikachu + n_otaku + n_pulpo + n_anguila}")
print("*" * 30)
print(f"Pikachu Roll ${n_pikachu}")
print(f"Otaku Roll ${n_otaku}")
print(f"Pulpo Venenoso Roll ${n_pulpo}")
print(f"Anguila Eléctrica Roll {n_anguila}")
print("*" * 30)
print(f"Subtotal por pagar: ${total_compra}")
print(f"Descuento por código: ${total_compra * desc}")
print(f"TOTAL: ${total_compra - total_compra * desc}")
