import  random
# Gets answer to wordle
Answer = random.choice(list(open("Words.txt"))).upper()
with open("Words.txt","r") as file:
    Content = file.read()
print("Wordle")
Guess_Counter = 0
while True: 
    Guess = input("Enter guess: ").upper()
    if Guess_Counter == 5 :
        print("The word was " + Answer)
        print("Better luck next time :(")
        break
    if isinstance(Guess, str) and Guess in Content.upper():
        if len(Guess) == 5:
            Guess_Counter += 1
            # start of checking letters in word
            answerletters = list(Answer)
            guessletters = list(Guess)
            output = ["." for i in range(len(Guess))]
            #checks for correct letter in correct position
            for count, value in enumerate(guessletters):
                if value == answerletters[count]:
                    output[count] = guessletters[count]
                    answerletters[count] = "."
                    guessletters[count] = "." 
            #checks for correct letter in wrong position   
            for i, g_letter in enumerate(guessletters):
               for j, a_letter in enumerate(answerletters):
                    if (a_letter == g_letter) and (a_letter != "."):
                        output[i] = g_letter.lower()
                        answerletters[j] = "."
                        guessletters[i] = "."
                        break     
            print(" ".join(output))                        
            if Guess in Answer:
                print("Congratulations :)")
                break   
        else:
            print("Your word must contain five letters")
    else:
        print("Enter a real word")    
