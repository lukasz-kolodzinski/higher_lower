# Simple game 'Higher Lower'. User has to guess random number drawn by program.

import random

game_on = None
answers = None
magic_number = None

def easy_mode():
    global magic_number
    magic_number = int(random.randrange(0,11))
    global game_on
    game_on = True
    while game_on is True:
        user_guess = int(input('Guess the number from range 0-10: '))
        if user_guess > magic_number:
            print('Too high. Try again.')
        elif user_guess < magic_number:
            print('Too low. Try again.')
        else:
            print('Great! You won!')
            again = input('Do you want play again? Type YES or NO: ')
            if again == 'YES':
                easy_mode()
            else:
                quit()
