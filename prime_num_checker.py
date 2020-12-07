# prime number check
# prime number is only divisible by 1 and itself.

# define function
def prime_checker(number):
    is_prime = True
    for i in range(2, number - 1):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print(f"{number} is a Prime Number.")
    else:
        print(f"{number} is NOT a Prime Number.")


# gather number to check
n = int(input("Check this number: "))

num_length = str(n)

if len(num_length) > 8:
    print("That number is too big, it will crash the computer.")
else:
    # call prime checker func
    prime_checker(number=n)
