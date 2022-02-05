rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

rps = [rock, paper, scissors]

rps_user = int(input("choose 1 for rock, 2 for paper, or 3 for scissors: "))

print(rps[rps_user - 1])

rpscomp = random.randint(1,3)

print(f"Computer chose: {rpscomp}\n{rps[rpscomp - 1]}")

if (rps_user == 1 and rpscomp == 3) or (rps_user == 2 and rpscomp == 1) or (rps_user == 3 and rpscomp == 2):
    print("You won.")

elif rps_user == rpscomp:
    print("Tie game.")

else:
    print("You lose.")