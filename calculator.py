# ask for first num
# ask for operation
# ask for second num
# display result
# then
# ask to continue or start new operation
# if new operation - start again
# if continue - ask for next operation
# ask for another number
# display result
# ask to continue or start new operation

# operation funcs

# add
def add(n1, n2):
    '''Adds two numbers together'''
    return n1 + n2


def subtract(n1, n2):
    '''Subtracts n2 from n1'''
    return n1 - n2


def multiply(n1, n2):
    '''Multiplies two numbers together'''
    return n1 * n2


def divide(n1, n2):
    '''Divide n1 / n2'''
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calc():
    num1 = float(input("What's the first number?: "))

    # print operation options
    for op in operations:
        print(op)

    continue_calc = True

    while continue_calc:

        op_chosen = input("Please selct an Operation: ")

        num2 = float(input("What's the next number?: "))

        # get the value from the op chosen and add the params of num1 and num2
        calculation = operations[op_chosen]
        answer = calculation(num1, num2)

        print(f"{num1} {op_chosen} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating {answer}, or type 'n' to start a new calculation: ") == "y":
            num1 = answer
        else:
            continue_calc = False
            calc()


calc()
