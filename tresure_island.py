# adventure game style

print("Welcome to Treasure Island!\nYour mission is too find the treasure.")

first_direction = input(
    "You arrive at the island, you can go Left or Right. Where do you want to go?\n")
if first_direction.lower() == "right" or first_direction.lower() == "go right":
    print("You have fallen into a pit. Bad luck mate.")
elif first_direction.lower() == "left" or first_direction.lower() == "go left":
    print("You move forward through the island, making good progress.")

    wall_decision = input(
        "You come to a tall brick wall, do you want to walk around it or climb over it?\n")
    if wall_decision.lower() == "climb it" or wall_decision.lower() == "climb over":
        print("Oof, you fell and died mate. Game over.")
    elif wall_decision.lower() == "walk" or wall_decision.lower() == "walk around":
        print("You chose wisely!")

        door_decision = input(
            "There are two doors. Yellow and Green. Which one has the Treasure behind it?\n")
        if door_decision.lower() == "yellow":
            print("Well Done, you have found the treasure!")
        elif door_decision.lower() == "green":
            print(
                "A lion has jumped out of the door as you opened it. You did not survive.")
        else:
            print("you didn't make a valid choice, you died from malnutrition.")
    else:
        print("you didn't make a valid choice, you died from malnutrition.")
else:
    print("you didn't make a valid choice, you died from malnutrition.")
