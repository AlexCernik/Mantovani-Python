ingreso = float(input('Introduzca el ingreso: '))

if ingreso < 85718:
    calculo = (ingreso * 0.18) - 596
    if calculo < 0:
        print('El impuesto es: 0.0 pesos')
    else:
        print(f'El impuesto es: {(ingreso * 0.18) - 596:.0f}.0 pesos')
else:
    print(f'El impuesto es: {((ingreso - 85718) * 0.32) + 14319:.0f}.0 pesos')