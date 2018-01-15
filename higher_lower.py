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
        user_guess = int(input('Welcome in Easy Mode! Guess the number from range 0-10: '))
        if user_guess > magic_number:
            print('Too high. Try again.')
        elif user_guess < magic_number:
            print('Too low. Try again.')
        else:
            print('Great! You won!')
            play_again()
#            again = input('Do you want play again? Type YES or NO: ')
#            if again == 'YES':
#                easy_mode()
#            else:
#                quit()

def game_start():
    global game_on
    game_on = True
    game_behavior = input('Choose game level or quit. Type: EASY or HARD or QUIT: ')
    if game_behavior == 'EASY':
        easy_mode()
    elif game_behavior == 'HARD':
        hard_mode()
    else:
        game_on = False
        print('Bye. See you soon!')

def play_again():
    global game_on
    game_on = True
    new_game = input('Do you want to play again? Type YES or NO: ')
    if new_game == 'YES':
        game_start()
    else:
        game_on = False

game_start()
