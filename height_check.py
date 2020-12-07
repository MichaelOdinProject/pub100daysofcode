# height example
height = int(
    input("welcome to the rollercoaster\nWhat is your height in centimetres???\n"))

bill = 0

if height >= 120:
    print("You can go on the rollercoaster!")
    age = int(input("What age are you?\n"))
    if age >= 18:
        print("That will cost £15 please.")
        bill = 15
    elif age <= 17 and age >= 12:
        print("That will cos £12 please.")
        bill = 12
    else:
        print("That will cost £6 punds please.")
        bill = 6

    want_photo = input("DO you want a photo taken also, Y or N.\n")
    if want_photo == "Y" or want_photo == "y":
        print(f"That brings your total to £{bill + 3}")
    else:
        print(f"That brings your total to £{bill}")
else:
    print("You are to short, sorry!")
