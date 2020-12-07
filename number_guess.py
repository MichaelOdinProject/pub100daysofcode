# ask easy or hard mode - easy 5 attempt - hard 10 attempts
# generate random num

# LOOP
# user guess
# say too high or too low
# user guess
# say too high or too low
# LOOP


import random


def game_difficulty(game_mode):
    '''take difficulty chosen and return num of guesses left'''
    if game_mode.lower() == "easy":
        return 5

    elif game_mode.lower() == "hard":
        return 10
    else:
        return "no game"


def guessing_game(guess, actual_num):
    '''Takes user guess, generated num and compares for gussing game'''
    if guess < actual_num:
        return "Your guess was too low!"
    elif guess > actual_num:
        return "Your guess is too high!"
    else:
        return "Your guess was CORRECT!!"


####Guessing Game begins####
print("Welcome")
print("In this game, you need to guess the number between 1 and 100")
print("++++++" * 5)

game_mode = input("Do you want to play on 'easy' or 'hard' mode?: ")
guesses_left = game_difficulty(game_mode)
if guesses_left == "no game":
    print("Invalid Choice!")
    exit()

# generate a target number to guess
generated_num = random.randint(1, 100)

continue_game = True

while continue_game:

    user_guess = int(input("What is your guess?:  "))

    result = guessing_game(user_guess, generated_num)
    print(result)
    if result == "Your guess was CORRECT!!":
        continue_game = False

    guesses_left -= 1
    if guesses_left == 0:
        print("You're out guesses! Game over")
        continue_game = False
