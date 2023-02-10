'''Guess the number'''

import random

def generator_dict():
    return random.randint(1, 10)

try_count = 1

print('''Hi, let’s play the game Guess the number
guess we will be the numbers from 1 to 10
have a nice game and good luck''')

print()

while True:

    try:
        if int(input('Enter number -> ')) != generator_dict():
            print(f'Try again \nThat was your attempt number: {try_count}')
            try_count += 1
        else:
            print(f'Your WIN  \nYou guessed from: {try_count} spits\nIf you want to play another write yes if not no')
            a = str(input('Yes or No -> '))

            if a[0] in 'Nn':
                print('Goodbye')
                break
            elif a[0] in 'Yy':
                try_count = 1

    except:
        print('Enter number from 1 to 10 ')