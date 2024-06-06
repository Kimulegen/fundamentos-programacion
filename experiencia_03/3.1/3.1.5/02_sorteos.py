#! Python3
# Lottery simulator

import os
import random

# initialize variables
user_ticket = []

# ask user for 7 lucky numbers, show them
print("Ingrese sus 7 números de la suerte")
for i in range(7):
    user_ticket.append(int(input(f"Ingrese número: ")))
os.system("cls||clear")
print("Usted ingresó los siguientes números:", user_ticket)

# 3 games, each one with different winner numbers
for round in range(3):
    print(f"Los números sorteados en la ronda {round + 1} fueron")

    # pick random winner numbers
    lottery = []
    for i in range(7):
        while True:
            number = random.randint(1, 49)
            if lottery.count(number) == 0:
                lottery.append(number)
                break
        print(number)

    # compare winner numbers with user numbers
    if sorted(user_ticket) == sorted(lottery):
        print("Ganaste!")
    else:
        print("Lo siento, pero no has ganado en esta ronda")

    print()
