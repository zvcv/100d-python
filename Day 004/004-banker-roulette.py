import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# -1 karena randint mulai dari 0, 1, 2, dst
# padahal len(names) nya mulai dari 1, 2, 3, dst
# jadi biar jumlah randint nya sama dengan len(names) di -1
name = names [random.randint(0,(len(names)-1))]

# simpler way below
# name = random.choice(names)

print (f"{name} is going to buy the meal today!")