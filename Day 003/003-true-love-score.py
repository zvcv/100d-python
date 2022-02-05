# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs. 
# Then check for the number of times the letters in the word LOVE occurs. 
# Then combine these numbers to make a 2 digit number.

#Write your code below this line 👇

name = name1.lower() + name2.lower()

score1 = name.count ("t") + name.count ("r") + name.count ("u") + name.count ("e")
score2 = name.count ("l") + name.count ("o") + name.count ("v") + name.count ("e")
score = int(f"{score1}{score2}")

if score < 10 or score > 90:
    print (f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print (f"Your score is {score}, you are alright together.")
else:
    print (f"Your score is {score}.")