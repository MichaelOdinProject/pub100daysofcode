# fizz buzz game
# should print each number from 1-100 in turn
# when num is divisible by 3 print "fizz"
# when num is divisible by 5 print "buzz"
# if divisible by both 3 and 5 print "FizzBuzz"


for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
