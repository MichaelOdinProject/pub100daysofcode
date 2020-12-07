# the ceasar cipher will take a letter and shift it in the alphabet based of the SHIFT number given
from caesar_cipher_alphabet_bank import alphabet
# Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f"The {cipher_direction} text is {end_text}")


acceptable_direction = ['encode', 'decode']

direction = input(
    "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# make sure accepatble direction chosen
if direction not in acceptable_direction:
    print("Choice not regocnised.")
    exit()


text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# check if user wants to Decrypt or Encrypt
caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
