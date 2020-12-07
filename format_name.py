# Functions with outputs

# def format_name(f_name, l_name):
#     full_name = f_name + " " + l_name

#     return full_name.title()

# full_name = format_name("michael", "mcguire")
# print(full_name)


# You can put the inputs into the function right away
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't enter a name!"
    full_name = f_name + " " + l_name

    return full_name.title()


print(format_name(input("What is your first name?: "),
                  input("What is your second name?: ")))
