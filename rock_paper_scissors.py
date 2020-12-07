# Rock wins against scissors
# Scissors win against paper
# Paper wins against rock

import random

print("Welcome to Rock, Paper, Scissors.")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

machine_choice = random.randint(0, 2)
print("Machine has chosen:")
print(game_images[machine_choice])

if user_choice >= 3 or user_choice < 0:
    print("You made an invalid choice, you LOSE!")
elif user_choice == 0 and machine_choice == 2:
    print("YOU WIN")
elif machine_choice == 0 and user_choice == 2:
    print("YOU LOSE")
elif machine_choice > user_choice:
    print("YOU LOSE")
elif user_choice > machine_choice:
    print("YOU WIN")
elif user_choice == machine_choice:
    print("DRAW")
