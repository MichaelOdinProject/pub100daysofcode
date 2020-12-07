total_bill = float(input("What was the total bill? \n"))
percentage_tip = int(
    input("What percentage of tip would you like to give? 10, 12 or 15? \n"))
split_num = int(input("How many people to split the bill? \n"))

tip_as_decimal = percentage_tip / 100 + 1
after_tip_bill = total_bill * tip_as_decimal

split_bill = round(after_tip_bill / split_num, 2)

print(f"Each person should pay: ${split_bill}")
