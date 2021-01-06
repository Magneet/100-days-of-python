weight = int(input("whats your weight?\n"))
height = float(input("whats your height?\n"))
bmi = weight / (height ** 2)

bmi = round(bmi, 2)
if bmi <= 18.5:
    print(f"BMI of {bmi} is under 18.5")
elif bmi <= 25:
    print(f"BMI of {bmi} is under 25")
elif bmi <= 30:
    print(f"BMI of {bmi} is under 30")
elif bmi <= 35:
    print(f"BMI of {bmi} is under 35")
elif bmi > 35:
    print(f"BMI of {bmi} is over 35")