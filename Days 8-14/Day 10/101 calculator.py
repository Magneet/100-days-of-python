def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2

def multiply(n1, n2):
    return n1 * n2

operations = {
    "+":add,
    "-":subtract,
    "/":divide,
    "*":multiply,
}
first = True
num1 = float(input("WHat's the first number\n"))

calc = True
while calc == True:
    if first ==True:
        num2 = float(input("WHat's the second number\n"))
    else:
        num2 = float(input("WHat's the next number\n"))
    for symbol in operations:
        print(symbol)
    operation_symbol = input("Pick an operation symbol from the lines above\n")
    result =  operations[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {result}")
    num1 = result
    again = input(f"type 'y' to continu calculating with {result}, n to start over or anything else to exit")
    if again == "y":
        first = False
        calc = True
    elif again == "n":
        first = True
        calc = True
    else:
        calc = False

