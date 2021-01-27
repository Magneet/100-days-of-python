with open("D:\\GIT\\100-days-of-python\\Days 22-29\\Day 23\\ex\\file1.txt") as file1:
    data_file1 = file1.readlines()

with open("D:\\GIT\\100-days-of-python\\Days 22-29\\Day 23\\ex\\file2.txt") as file2:
    data_file2=file2.readlines()


result = [int(n) for n in data_file1 if n in data_file2]
print(result)