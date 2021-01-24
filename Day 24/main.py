dir = "d:\\GIT\\100-days-of-python\\Day 24\\"

with open(f"{dir}text.txt", mode="a") as file:
    file.write("\nfdfddffsdfdsfsdfsd\n")

with open(f"{dir}text.txt") as file:
    contents = file.read()
    print(contents)

