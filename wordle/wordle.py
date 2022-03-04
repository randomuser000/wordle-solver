f = open("C://Users//thrya//OneDrive//Documents//code//wordle//words.txt", "r")       #open text file with list of 5 letter words to read

green = ['', '', '', '', '']      #array for letters in correct spot
yellow = ['', '', '', '', '']     #array for letters in word but wrong spot
black = []      #array for letters not in word
possibleWords = []

loopInt = 0

allWordsArray = []
for wordInFile in f:
    newWord = wordInFile.replace("\n", "")
    allWordsArray.append(newWord)

def checkValidWords():
    global green
    global yellow 
    global black 
    global possibleWords 
    global allWordsArray 

    for word in allWordsArray:
        wordArr = list(word)
        wordPossible = True
        greenLoopInt = 0
        yellowLoopInt = 0
        if wordPossible == True:
            for i in range(5):
                if green[greenLoopInt] != '':
                    if green[greenLoopInt] == wordArr[greenLoopInt]:
                        wordPossible = True
                    if green[greenLoopInt] != wordArr[greenLoopInt]:
                        wordPossible = False
                        break
                else:
                    pass
                greenLoopInt += 1
        if wordPossible == True:
            for i in range(5):
                if yellow[yellowLoopInt] != '':
                    if yellow[yellowLoopInt] not in word:
                        wordPossible = False
                        break
                    if yellow[yellowLoopInt] == wordArr[yellowLoopInt]:
                        wordPossible = False
                        break
                    if yellow[yellowLoopInt] in word:
                        wordPossible = True
                else:
                    pass 
                yellowLoopInt += 1
        if wordPossible == True:
            for letter in black:
                if letter in word:
                    wordPossible = False
                    break
                if letter not in word:
                    wordPossible = True
        if wordPossible == True:
            possibleWords.append(word)
    print(possibleWords)

guess1 = input("enter your first guess (ex: great)")   #ask for 1st guess
clues1 = input("enter the colors of the letters in order (g = green, y = yellow, b = black; ex: gybbb)") #ask for clues from 1st guess
guess1arr = list(guess1)    #convert word into an array
clues1arr = list(clues1)    #convert clues into an array

for i in range(5):
    if clues1arr[loopInt] == "g":
        green[loopInt] = guess1arr[loopInt]
    if clues1arr[loopInt] == "y":
        yellow[loopInt] = guess1arr[loopInt]
    if clues1arr[loopInt] == "b":
        black.append(guess1arr[loopInt])
    loopInt += 1
loopInt = 0

checkValidWords()

guess2 = input("enter your second guess (ex: great)")   #ask for 1st guess
clues2 = input("enter the colors of the letters in order (g = green, y = yellow, b = black; ex: gybbb)") #ask for clues from 1st guess
guess2arr = list(guess2)    #convert word into an array
clues2arr = list(clues2)    #convert clues into an array

for i in range(5):
    if clues2arr[loopInt] == "g":
        green[loopInt] = guess2arr[loopInt]
    if clues2arr[loopInt] == "y":
        yellow[loopInt] = guess2arr[loopInt]
    if clues2arr[loopInt] == "b":
        black.append(guess2arr[loopInt])
    loopInt += 1
loopInt = 0

possibleWords.clear()
checkValidWords()

guess3 = input("enter your third guess (ex: great)")   #ask for 1st guess
clues3 = input("enter the colors of the letters in order (g = green, y = yellow, b = black; ex: gybbb)") #ask for clues from 1st guess
guess3arr = list(guess3)    #convert word into an array
clues3arr = list(clues3)    #convert clues into an array

for i in range(5):
    if clues3arr[loopInt] == "g":
        green[loopInt] = guess3arr[loopInt]
    if clues3arr[loopInt] == "y":
        yellow[loopInt] = guess3arr[loopInt]
    if clues3arr[loopInt] == "b":
        black.append(guess3arr[loopInt])
    loopInt += 1
loopInt = 0

possibleWords.clear()
checkValidWords()

guess4 = input("enter your fourth guess (ex: great)")   #ask for 1st guess
clues4 = input("enter the colors of the letters in order (g = green, y = yellow, b = black; ex: gybbb)") #ask for clues from 1st guess
guess4arr = list(guess4)    #convert word into an array
clues4arr = list(clues4)    #convert clues into an array

for i in range(5):
    if clues4arr[loopInt] == "g":
        green[loopInt] = guess4arr[loopInt]
    if clues4arr[loopInt] == "y":
        yellow[loopInt] = guess4arr[loopInt]
    if clues4arr[loopInt] == "b":
        black.append(guess4arr[loopInt])
    loopInt += 1
loopInt = 0

possibleWords.clear()
checkValidWords()

guess5 = input("enter your fifth guess (ex: great)")   #ask for 1st guess
clues5 = input("enter the colors of the letters in order (g = green, y = yellow, b = black; ex: gybbb)") #ask for clues from 1st guess
guess5arr = list(guess5)    #convert word into an array
clues5arr = list(clues5)    #convert clues into an array

for i in range(5):
    if clues5arr[loopInt] == "g":
        green[loopInt] = guess5arr[loopInt]
    if clues5arr[loopInt] == "y":
        yellow[loopInt] = guess5arr[loopInt]
    if clues5arr[loopInt] == "b":
        black.append(guess5arr[loopInt])
    loopInt += 1
loopInt = 0

possibleWords.clear()
checkValidWords()