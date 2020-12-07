import random

from hangman_wordlist import word_list
from hangman_stages import stages
# def guess_check(guess, chosen_word, blanks, player_lives):
#     for position in range(len(chosen_word)):
#         letter = chosen_word[position]
#         if letter == guess:
#             blanks[position] = letter

#     print(blanks)

#     if guess not in chosen_word:
#         player_lives -= 1
#         print(player_lives)
#         if player_lives == 0:
#             end_of_game = True
#             print("You Lose")


#########CODE BEGINS##########
player_lives = 6
# intial word bank


# randomly choose word from list
# assign to variable chosen_word
chosen_word = random.choice(word_list)
print(f"This is the word for testing ONLY: {chosen_word}")

# create list of blanks for the word ["_", "_"]
blanks = []
for _ in range(len(chosen_word)):
    blanks += "_"
print(blanks)

# create While loop for repeated guessing
end_of_game = False
while end_of_game == False:

    # ask user to guess letter
    # assign answer to variable guess(lowercase)
    guess = input("\nPlease guess a letter:\n").lower()
    # check if letter is in chosen_word
    # for position in range(len(chosen_word)):

    # check if guess ahs already been made
    if guess in blanks:
        print("You have already guessed this letter")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            blanks[position] = letter

    print(blanks)

    if guess not in chosen_word:
        print(f"You guessed {guess}, that is not in the word.")
        player_lives -= 1
        print(f"You have {player_lives} lives left!")
        if player_lives == 0:
            end_of_game = True
            print("You Lose")

    # check if any remaining blanks
    if not "_" in blanks:
        end_of_game = True
        print("\nWell Done, You won!")

    # print the stages
    print(stages[player_lives])
