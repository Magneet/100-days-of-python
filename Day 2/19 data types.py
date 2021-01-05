while True:
    try:
        twodigit = int(input("give a 2 digit number\n"))
        break
    except:
        print("That's not a valid option!")
twodigits = str(twodigit)
firstdigit = int(twodigits[0])
seconddigit = int(twodigits[1])
calcdigits = firstdigit+seconddigit
print(calcdigits)