import re
import string

text = input('Por favor ingrese un texto: ')

letters = input('Por favor ingrese tres letras: ')

data_letter_user = {}

for i in letters:
    count_letter = 0
    for k in text:
        if i.lower() == k.lower() and i.isalpha():
            count_letter += 1
    data_letter_user.update({
        i: count_letter
    })

chars = re.escape(string.punctuation)
lett = re.sub(r'['+chars+']', '', text).split()

data_text = {
    'count_letters': len(lett)
}

for i in lett:
    if i in data_text:
        data_text.update({
            i: data_text[i] + 1
            })
    else:
        data_text.update({
            i: 1
            })

for k, v in data_letter_user.items():
    print(f'{k} aparece: {v} veces.')

for k, v in data_text.items():
    if k == 'count_letters':
        print(f'Cantidad de palabras en el texto, {v}.\n')
    else:
        print(f'La palabra {k} aparece: {v} veces.')

print(text[::-1])
