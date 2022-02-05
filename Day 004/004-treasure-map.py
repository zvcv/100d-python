# 🚨 Don't change the code below 👇
from turtle import pos


row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# if int(position[1]) == 1:
#     row1[int(position[0])-1] = "X"

# elif int(position[1]) == 2:
#     row2[int(position[0])-1] = "X"

# elif int(position[1]) == 3:
#     row3[int(position[0])-1] = "X"

# else:
#     print("you entered the wrong formula.")

# simpler way 👇

horizontal = int(position[0])
vertical = int(position[1])

selected_row = map[vertical - 1]
selected_row[horizontal - 1] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")