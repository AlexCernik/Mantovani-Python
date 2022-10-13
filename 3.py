def esPrimo(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def main():
    num_input = int(input('Ingrese un número: '))
    for i in range(2, num_input + 1):
        if esPrimo(i):
            print(i)
main()