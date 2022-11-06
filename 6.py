import random

numbers = random.choices([f'{i:02d}' for i in range(0, 100)], k=20)
tickets = []

wins = {
    5: 0,
    6: 0,
    7: 0,
    8: 0,

}

try:
    ticket_count = int(input('Ingrese la cantidad de boletas: '))
except TypeError:
    print('Debe ingresar solo número.')
else:

    for i in range(0, ticket_count):
        tickets.append(random.choices([f'{i:02d}' for i in range(0, 100)], k=8))

    
    for i in tickets:
        count_acert = 0
        for k in i:
            if k in numbers:
                # print(k)
                count_acert += 1
        # print(count_acert)
        if count_acert == 5:
            wins[5] += 1
        elif count_acert == 6:
            wins[6] += 1
        elif count_acert == 7:
            wins[7] += 1
        elif count_acert == 8:
            wins[8] += 1

print(
    f"""
        5 aciertos: {wins[5]}
        6 aciertos: {wins[6]}
        7 aciertos: {wins[7]}
        8 aciertos: {wins[8]}
    """
)
