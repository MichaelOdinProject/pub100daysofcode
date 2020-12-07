# password generator
# ask how many letter, symbols and numbers they would like
# produce password

# Password Generator Project
import random
letters = ['a' 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
ch_letters = int(input("How many letters would you like in your password?\n"))
ch_symbols = int(input(f"How many symbols would you like?\n"))
ch_numbers = int(input(f"How many numbers would you like?\n"))

# ########################
# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# easy_password = ""
# # Apply Letters to password
# for letter in range(1, ch_letters + 1):
#     # random_char = random.choice(letters)
#     # password = password + random_char
#     # but can be simplified to this:
#     easy_password += random.choice(letters)

# # Apply Symbols to password
# for sym in range(1, ch_symbols + 1):
#     easy_password += random.choice(symbols)

# # Apply Numbers to password
# for num in range(1, ch_numbers + 1):
#     easy_password += random.choice(numbers)

# print(f"Your new password is {easy_password}")

#########################
# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

hard_password = []

# Apply Letters to password
for letter in range(1, ch_letters + 1):
    # random_char = random.choice(letters)
    # password = password + random_char
    # but can be simplified to this:
    hard_password += random.choice(letters)

# Apply Symbols to password
for sym in range(1, ch_symbols + 1):
    hard_password += random.choice(symbols)

# Apply Numbers to password
for num in range(1, ch_numbers + 1):
    hard_password += random.choice(numbers)

random.shuffle(hard_password)
solid_password = ""
solid_password = solid_password.join(hard_password)
print(f"Your complex password is {solid_password}")
