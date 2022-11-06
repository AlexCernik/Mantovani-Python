import random

words = []

while True:
    enter_list_words = input('Ingrese un texto para guardar algunas palabras: ').split()
    
    for i in enter_list_words:
        if i.isalpha() and len(i) > 4:
            words.append(i)
    break

word = random.choice(words)
data_printable = ['_ ' for i in word]
life = len(word)
print(''.join(data_printable))

while True:
    letter = input('Ingrese una letra: ')

    if not letter.isalpha():
        print('\nDebe ingresar solo letas.')
    else:

        if letter in data_printable:
            print(
            """
**********************************************
*  Ya elegiste esta letra, prueba con otra.  *
**********************************************
            """)
        elif letter in word:
            for i in range(0, len(word)):
                if word[i] == letter:
                    data_printable[i] = letter
        elif letter not in word:
            print(f'\nPierdes 1 vida, vidas restantes {life}.')
            life -= 1

        print(''.join(data_printable))
        
        
        if life == 0:
            print(
                """
****************
*  ¡Perdiste!  *
****************
            """
            )
            break
        if word == ''.join(data_printable):
            print(
                """
***************
*  ¡Ganaste!  *
***************
            """
            )
            break