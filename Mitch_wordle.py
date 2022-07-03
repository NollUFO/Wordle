word = input().upper()
guess = input().upper()

wordletters = list(word) #word letters is a list composed of the letters in the word variable
guessletters = list(guess) #guessletters is a list composed of letters in the guess variable
output = [".",".",".",".","."] #output is a list of letters that contribute to what will be outputted; it is initialized to be (.....)

#Loop 1 - finding the letters that are IN THE CORRECT POSITION
for i,letter in enumerate(guessletters): #loop through guessletters (i.e. the letters in the guess varibale)
    if letter == wordletters[i]: #if the letter is correct (matches the word variable) then update the output variable to show a correct letter
        output[i] = guessletters[i]
        wordletters[i] = "." #also: if the letter is correct (matches the word variable) then update wordletters and guessletters to "remove" the letter that has aready been considered in terms of the output variable
        guessletters[i] = "."

#Loop 2 - finding the letters that are CORRECT but IN THE WRONG POSITION 
for i,g_letter in enumerate(guessletters): #loop through guessletters again
    for j,w_letter in enumerate(wordletters): #also loop through wordletters
        if (w_letter == g_letter) and (w_letter != "."): # if the wordletter has not been considered by the first loop above, and the letter matches a letter in the guessword then update output to show that the guessed letter is correct, but just in the wrong place
            output[i] = g_letter.lower() #update output to show this
            wordletters[j] = "."  #also: if the letter is correct (but in the wrong place) then update wordletters and guessletters to "remove" the letter that has aready been considered in terms of the output variable
            guessletters[i] = "."
            break
print("".join(output)) #the .join will just join all the characters in the list and form an actual string to be outputted