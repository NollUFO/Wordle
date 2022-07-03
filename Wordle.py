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
            feedback = list(Guess)
            accurate = []
            inaccurate = []
            for count, value in enumerate(Guess):
                if value == Answer[count]:
                    feedback[count] = '\033[1m' + value + '\033[0m' 
                    accurate.append(count)
            for i,k in enumerate(Guess):
                for j,l in enumerate(Answer):
                    if j in inaccurate or j in accurate:
                        continue
                    if k == l:
                        feedback[i] == '\033[4m' + k + '\033[0m'
                        inaccurate.append(j)
                        break
            for i in range(len(feedback)):
                if i not in accurate:
                    feedback[i] = '\033[4m' + feedback[i] + '\033[0m'    
#                    chars_guess[count] = '\033[4m' + value + '\033[0m' 
#                    if value == chars_answer[count]:
#                        chars_guess[count] = '\033[1m' + value + '\033[0m'  
            print(" ".join(feedback))             
            if Guess in Answer:
                print("Congratulations :)")
                break   
        else:
            print("Your word must contain five letters")
    else:
        print("Enter a real word")    