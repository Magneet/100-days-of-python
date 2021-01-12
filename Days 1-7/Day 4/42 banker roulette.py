import random
#people = ["rob","hank","bruce"]
people = [input("Who's the first person?")]
people.append(input("Who's the second person?"))
people.append(input("Who's the third person?"))
banker = random.choice(people)
print(f"The person paying is {banker}")