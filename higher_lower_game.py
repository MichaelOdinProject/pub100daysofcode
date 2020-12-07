from higher_lower_game_art import logo, vs
from higher_lower_game_dict import data

import random


def format_data(account):
    '''Take account data and return in readable format'''
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, {account_desc}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    '''Take the user guess and follower counts and returns if they got it right'''
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


# Display Art
print(logo)

score = 0

account_b = random.choice(data)


# make game repeatable
game_should_continue = True
while game_should_continue:

    # generate random account
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    # ask user for guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # check if user is correct
    # get follower account num
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # give user feedback right wrong
    # score keeping
    if is_correct:
        score += 1
        print("####" * 8)
        print(f"CORRECT, Your current score is {score}")
    else:
        game_should_continue = False
        print("####" * 8)
        print(f"WRONG, your final score was {score}")

    # move account B move to position A

    # Clear the screen
