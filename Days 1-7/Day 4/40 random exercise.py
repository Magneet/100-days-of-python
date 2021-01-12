import random

#rnm = random.randint(20,200)

userchoice = input("heads or tails?")
userchoice = userchoice.lower()
computerchoice = random.randint(0,1)

if computerchoice == 1:
    computerchoice = "heads"
elif computerchoice == 0:
    computerchoice = "tails"

if userchoice == computerchoice:
    print(f"it was {computerchoice} you win!")
else:
    print(f"it was {computerchoice} you loose!")