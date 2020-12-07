# decide who pays the bill
# select a name from pool
import random

#####################CODE - 1#################################
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# split string method - put names into a list
nameAsCSV = input("Give me everybody's name, seperated by a coma. \n")
names = nameAsCSV.split(", ")
# get num of items in list
num_of_names = len(names)
random_decider = random.randint(0, num_of_names - 1)
bill_payer = names[random_decider]
# random num between 0 - max num in list
print(bill_payer + " is going to buy the meal today!")
#####################CODE - 1#################################

#####################CODE - 2#################################
# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)

# # # split string method - put names into a list
# nameAsCSV = input("Give me everybody's name, seperated by a coma. \n")
# names = nameAsCSV.split(", ")


# new_bill_payer = random.choice(names)
# print(new_bill_payer + " is going to buy the meal today!")

#####################CODE - 2#################################
