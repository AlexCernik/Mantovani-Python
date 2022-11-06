import random

data = {
    1: '-',
    2: '-',
    3: '-',
    4: '-',
    5: '-',
    6: '-',
    7: '-',
    8: '-',
    9: '-',
}

def data_table():
    table = \
        """
        ┌───┬───┬───┐
        │ {} │ {} │ {} │
        ├───┼───┼───┤
        │ {} │ {} │ {} │
        ├───┼───┼───┤
        │ {} │ {} │ {} │
        └───┴───┴───┘
        """.format(data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9])
    print(table)

count = 1
turn = ''
elections = []

def machine_complete():
    position = random.choice([number for number in range(1, 10) if number not in elections])
    data[position] = 'X'
    elections.append(position)
    print(f'\nLa compu juega la posición {position}')

def human_complete(value):
    # position = random.choice([number for number in range(1, 10) if number not in elections])
    if data[value] == '-':
        data[value] = 'O'
        elections.append(value)
    else:
        print('Esta posición ya está ocupada.')

machine_complete()


def win():
    status = None
    status_data = {
        'O': '¡Has Ganado!',
        'X': '¡La compu gana!'
    }

    if data[7] == data[8] == data[9] != '-':
        data_table()
        status = status_data[turn]
    elif data[4] == data[5] == data[6] != '-':
        data_table()
        status = status_data[turn]
    elif data[1] == data[2] == data[3] != '-':
        data_table()
        status = status_data[turn]
    elif data[1] == data[4] == data[7] != '-':
        data_table()
        status = status_data[turn]
    elif data[2] == data[5] == data[8] != '-':
        data_table()
        status = status_data[turn]
    elif data[3] == data[6] == data[9] != '-':
        data_table()
        status = status_data[turn]
    elif data[7] == data[5] == data[3] != '-':
        data_table()
        status = status_data[turn]
    elif data[1] == data[5] == data[9] != '-':
        data_table()
        status = status_data[turn]
    
    if count == 9:
        status = 'Empate.'

    return status

while True:
    data_table()

    try:
        value = int(input('Ingrese la posición la que quieres jugar: '))
    except TypeError:
        print('Debe ingresar solo número.')
    except ValueError:
        print("\nPor favor ingrese una posición para continuar.\n")
    else:
        if value < 1 or value >= 10:
            print('\nDebe ingresar un número del 1 al 9 por jugada.\n')
        else:
            if data[value] == '-':
            
                data[value] = 'O'
                elections.append(value)

                turn = 'O'
                count += 1
                if win() != None:
                    print(win())
                    break

                machine_complete()
                turn = 'X'
                count += 1
                if win() != None:
                    print(win())
                    break


            
