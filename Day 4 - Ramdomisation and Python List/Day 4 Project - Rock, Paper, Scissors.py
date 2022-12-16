rock_asci = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper_asci = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors_asci = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

signs = ["rock", "paper", "scissors"]
random_signs = random.choice(signs)

choice = int(input("What do yo choose? Type 0 for Rock, 1 for Paper 2 for Scissors."))

if choice == 0:
 users_sign = "rock1"
elif choice == 1:
 users_sign = "paper1"
elif choice == 2:
 users_sign = "scissors1"
else:
  print("invalid details")

if users_sign == "rock1" and random_signs == "scissors":
  print(f"{rock_asci}\nRock\n{scissors_asci}\nscissors\nYOU WIN")
elif users_sign == "rock1" and random_signs == "paper":
  print(f"{rock_asci}\nRock\n{paper_asci}\nPaper\nYOU LOST")
elif users_sign == "rock1" and random_signs == "rock":
  print(f"{rock_asci}\nRock\n{rock_asci}\nRock\nMATCH DRAWN")
elif users_sign == "paper1" and random_signs == "rock":
  print(f"{paper_asci}\nPaper\n{rock_asci}\nrock\nYOU WON")
elif users_sign == "paper1" and random_signs == "scissors":
  print(f"{paper_asci}\nPaper\n{scissors_asci}\nScissors\nYOU LOST")
elif users_sign == "paper1" and random_signs == "paper":
  print(f"{paper_asci}\nPaper\n{paper_asci}\nPaper\nMATCH DRAWN")
elif users_sign == "scissors1" and random_signs == "paper":
  print(f"{scissors_asci}\nscissors\n{paper_asci}\nPaper\nYOU WON")
elif users_sign == "scissors1" and random_signs == "rock":
  print(f"{scissors_asci}\nScissors\n{rock_asci}\nRock\nYOU LOST")  
elif users_sign == "scissors1" and random_signs == "scissors":
  print(f"{scissors_asci}\nScissors\n{scissors_asci}\nScissors\nMATCH DRAWN")
else:
  print("invalid detials")
