# find how many paint cans needed for area
# paint can can cover 5 square meters of wall
# number of cans = (wallheight x wallwidth) / coverage per can --- H=2 w=4 cov=5 (2x4)/5 = 1.6 (round up to 2)

import math

# define function


def paint_calc(height, width, coverage_per_can):
    num_of_cans = (height * width) / coverage_per_can
    num_of_cans = math.ceil(num_of_cans)
    print(f"You need to buy {num_of_cans} cans of paint to cover this.")


test_h = float(input(f"In Meters, Height of the wall: "))
test_w = float(input("In Meters, Width of the wall: "))
coverage_per_can = 5
paint_calc(height=test_h, width=test_w, coverage_per_can=coverage_per_can)
