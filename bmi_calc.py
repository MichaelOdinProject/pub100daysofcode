#bmi is weight(kg) / (height(m) * height(m))

# <18.5 is underweight
# >18.5 <25 is normal
# >25 <30 overweight
# >30 <35 obese
# >35 clinically obese

height = float(input("Please enter your height in m:\n"))
weight = float(input("Please enter your weight in kg:\n"))

bmi = round(weight / (height*height))

if bmi < 18.5:
    print(f"Your bmi of {bmi} indicates you are Underweight.")
elif bmi >= 18.5 and bmi < 25:
    print(f"Your bmi of {bmi} indicates you are a Normal Weight.")
elif bmi >= 25 and bmi < 30:
    print(f"Your bmi of {bmi} indicates you are Overweight.")
elif bmi >= 30 and bmi < 35:
    print(f"Your bmi of {bmi} indicates you are Obese.")
else:
    print(f"You bmi of {bmi} indicates you are Clinically Obese.")
