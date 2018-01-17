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
    print('Welcome in Easy Mode! Guess the number from range 0-10: ')
    while game_on is True:
        user_guess = int(input(""))
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

def hard_mode():
    global magic_number
    magic_number = int(random.randrange(0,11))
    global answers
    answers = 3
    answers_counter = 0
    print('Welcome in Hard Mode (you have only 3 attempts). Guess the number from range 0-10: ')
    while answers_counter < answers:
        user_guess = int(input(''))
        if user_guess > magic_number:
            print('Too high.')
            answers_counter = answers_counter + 1
        elif user_guess < magic_number:
            print('Too low.')
            answers_counter = answers_counter + 1
        elif user_guess == magic_number:
            print('Great! You won!')
            play_again()
    else:
        print('Game Over. ' + 'Correct number was: ' + str(magic_number))
        play_again()
        
def game_start():
    global game_on
    game_on = True
    game_behavior = input('Choose game level or quit. Type: EASY or HARD or QUIT: ')
    if game_behavior == 'EASY':
        easy_mode()
    elif game_behavior == 'HARD':
        hard_mode()
    elif game_behavior == 'QUIT':
        game_on = False
        print('Bye. See you soon!')
    else:
        print('Operation not allowed. Try again.')
        game_start()

def play_again():
    global game_on
    game_on = True
    new_game = input('Do you want to play again? Type YES or NO: ')
    if new_game == 'YES':
        game_start()
    else:
        game_on = False

game_start()
