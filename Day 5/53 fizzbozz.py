list = range(1, 101)
for number in list:
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
    elif number % 3 == 0 :
        print("fizz")
    el  if number % 5 == 0 :
        print("buzz")
    else:
        print(number)