# fruits = ["Apple", "Peach", "Pear"]

# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")


# calculate avg student height from lsit of heights

student_heights = input(
    "Input a list of student height, in cm and separated by a space:\n").split(" ")
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# print(student_heights)

# calc average of student heights
total_height = 0
for height in student_heights:
    total_height += height

num_of_students = 0
for student in student_heights:
    num_of_students += 1

average_height = total_height // num_of_students


print(f"The average height of the students in the list is {average_height}cm.")
