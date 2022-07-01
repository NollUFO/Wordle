import  random
# Gets answer to wordle
Answer = random.choice(list(open("Words.txt"))).upper()
with open("Words.txt","r") as file:
    Content = file.read()

print(Answer)
print("Wordle")
Guess_Counter = 0
while True: 
    Guess = input("Enter guess: ").upper()
    if Guess_Counter == 5 :
        print("Better luck next time :(")
        break
    if isinstance(Guess, str) and Guess in Content.upper():
        if len(Guess) == 5:
            Guess_Counter += 1
            # start of checking letters in word
            chars_guess = list(Guess)
            chars_answer = list(Answer)
            for count, value in enumerate(chars_guess):
                # check for duplicate characters
                guesschar_counter = 0
                anschar_counter = 0
                
                if value in chars_answer:
                    chars_guess[count] = '\033[4m' + value + '\033[0m' 
                    if value == chars_answer[count]:
                        chars_guess[count] = '\033[1m' + value + '\033[0m'    
            print(" ".join(chars_guess))             
            if Guess in Answer:
                print("Congratulations :)")
                break   
        else:
            print("Your word must contain five letters")
    else:
        print("Enter a real word")    