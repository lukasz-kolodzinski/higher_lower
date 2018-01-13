# Simple game 'Higher Lower'. User has to guess random number drawn by program.

import random

game_on = None
answers = None
magic_number = None

def easy_mode():
    global magic_number
    magic_number = int(random.randrange(0,100))
    while game_on:
        user_guess = int(input('Guess the number: '))
        if user_guess > magic_number:
            print('Too high. Try again.')
        elif user_guess < magic_number:
            print('Too low. Try again.')
        else:
            print('Great! You won!')
