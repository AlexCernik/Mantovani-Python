blocks = int(input('Ingrese la cantidad de bloques: '))
altura = 0
capa = 1

while capa <= blocks:

    altura += 1
    blocks -= capa
    capa += 1

print(f'La altura de la pirámide es: {altura}\nSobraron: {blocks} piezas')