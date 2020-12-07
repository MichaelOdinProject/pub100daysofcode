# mark a spot with an X.
# map is three rows of blank squares
# should be able to enter the position of treasue using a 2 digit system
# first digit - horizontal column
# second digit - vertical column

row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure?\n")

horizontal_position = int(position[0])
vertical_position = int(position[1])

selected_position = map[vertical_position - 1][horizontal_position - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")
