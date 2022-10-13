import random
import string

def random_password():
    rand_string = ''.join(
        random.sample(random.sample(string.ascii_letters, k=3) + 
        random.sample(string.digits, k=4) +
        random.sample(string.punctuation, k=3)
        , k=10)
    )

    password = ''
    for v in rand_string:
        left = rand_string.find(v) - 1

        if rand_string[left].isdigit() and v.isdigit():
             value = random.choice(string.punctuation) + v
        else:
                value = v
        password += value
    return password

print(random_password())



