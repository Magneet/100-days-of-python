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
import random
userchoice = input("Rock, paper or scissors?\n")
userchoicel = userchoice.lower()
rockpaperscissors = ["rock","paper","scissors"]
if not userchoicel in rockpaperscissors:
    print(f"{userchoice} is not a valid option")
    exit()

computerchoice = random.choice(rockpaperscissors)
print(f"Computer chooses {computerchoice} ")
if userchoicel == computerchoice:
    print("Similar")
elif userchoicel == "rock" and computerchoice == "paper":
    print("Computer wins")
elif userchoicel == "paper" and computerchoice == "scissors":
    print("Computer wins")
elif userchoicel == "scissors" and computerchoice == "rock":
    print("Computer wins")
elif userchoicel == "rock" and computerchoice == "scissors":
    print("player wins")
elif userchoicel == "paper" and computerchoice == "rock":
    print("player wins")
elif userchoicel == "scissors" and computerchoice == "paper":
    print("player wins")
