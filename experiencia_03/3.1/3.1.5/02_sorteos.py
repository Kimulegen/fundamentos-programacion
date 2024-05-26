import random

user_ticket = []
print('Ingrese sus 7 números de la suerte')
for i in range(7):
    user_ticket.append(int(input(f'Ingrese número: ')))

print('Usted ingresó los siguientes números:', user_ticket)

for round in range(3):
    print(f'Los números sorteados en la ronda {round + 1} fueron')

    lottery = []
    for i in range(7):
        while True:
            number = random.randint(1,49)
            if (lottery.count(number) == 0):
                lottery.append(number)
                break
        print(lottery[len(lottery)-1])
    
    if (sorted(user_ticket) == sorted(lottery)):
        print('Ganaste!')
    else:
        print('Lo siento, pero no has ganado en esta ronda')
    
    print()