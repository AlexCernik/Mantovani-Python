califications = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
sum_califications = 0
approved = 0

while True:
    try:
        calification = int(input('Ingrese la nota del alumno: '))
    except:
        print('Debe ingresar solo números.')
    else:
        if calification == 0:
            cant_califications = 0
            for i in califications:
                cant_califications += i

            if cant_califications:
                print(f'\n\nEl promedio es : {sum_califications/cant_califications:.2f}\n'
                      f'Aprobaron {approved} alumnos de {cant_califications} evaluados.\n\n'
                      f'El histograma es :\n ')

                for i in range(1, 11):
                    print(f'{i}{"  " if i == 10 else "   "}{"*" * califications[i-1]}')
            break

        elif calification < 1  or calification > 10:
            print('Debe ingresar números enteros del 1 a 10.')

        for i in range(1, 11):
            if calification == i:
                sum_califications += i
                califications[i - 1] += 1
                if calification >= 6:
                    approved += 1
