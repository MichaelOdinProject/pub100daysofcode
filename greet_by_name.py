# simple - write func to greet someone by their name
##############get name#########
# define greet function
def greet(name):
    print(f"Hello {name}, nice to meet you!")


# get user name
name = input("What is your name?\n").title()
# call function
greet(name)


##############get name, location#########
def greet_name_location(name, hometown):
    print(f"Hello {name}, I know you are from {hometown}")


name = input("What is your name?\n").title()
hometown = input("What city are you from?\n").title()

greet_name_location(name, hometown)
