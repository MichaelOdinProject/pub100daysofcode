# work out final bill based on users order
# small pizza = £15
# medium pizza = £20
# large pizza = £25

# pepperoni for small pizza = +£2
# pepperoni for med/large pizza = +£3
# extra cheese for any size = +£1

bill = 0

print("Welcome to the Pizza Place!")
size = input("What size of pizza do you want? S, M or L\n")
add_pepperoni = input("Do you want Pepperoni? Y or N\n")
extra_cheese = input("Do you want extra cheese? Y or N\n")

if size == "S" or size == "s":
    bill += 15
elif size == "M" or size == "m":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y" or add_pepperoni == "y":
    if size == "S" or size == "s":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y" or extra_cheese == "y":
    bill += 1

print(f"Thank you! Your order costs £{bill}")
