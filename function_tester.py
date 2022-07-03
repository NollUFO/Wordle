def is_word(line, list_content):
    if not isinstance(line, str) or not len(line) == 5 or not line in list_content: 
        return True

import random
Answer = random.choice(list(open("Words.txt"))).upper()
with open("Words.txt","r") as file:
    Content = file.read()

guess = input("Enter guess: ")
if is_word(guess, Content):
    print("Please enter a valid word")

guesslist = list(guess)
answerlist = list(Answer)
charcounter 
