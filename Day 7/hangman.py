import random
from hangman_words import word_list
from hangman_art import stages, logo


word = random.choice(word_list)
print(logo)
print(word)

answer = []
for x in range(len(word)):
    answer += "_"
tries = 7
word_list = list(word)
answer_list = []
while tries > 0 and word_list != answer:
    print(answer) 
    guessed_letter = input("Guess a letter\n")
    if guessed_letter in answer_list:
        print(f"You already tried the letter {guessed_letter}")
    elif guessed_letter in word:
        print(f"The letter {guessed_letter} is in the word.")
        for index, letter in enumerate(word):
            if guessed_letter == letter:
                answer[index] = letter
    else:
        tries -= 1
        print(f"The word doesn't contain {guessed_letter}.")
    print(f"You have {tries} attempts left")
    print(stages[tries])
    answer_list += guessed_letter

if tries == 0:
    print("game over")
elif word_list == answer and tries > 0:
    print("you won")