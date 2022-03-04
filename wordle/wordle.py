from pathlib import Path
import streamlit as st

p = Path(__file__).with_name('words.txt')
f = open(p, "r")       #open text file with list of 5 letter words to read

green = ['', '', '', '', '']      #array for letters in correct spot
yellow = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']     #array for letters in word but wrong spot
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
            for x in range(5):
                if yellow[yellowLoopInt] != '':
                    if yellow[yellowLoopInt] in word:
                        wordPossible = True
                    if yellow[yellowLoopInt] not in word:
                        wordPossible = False
                        break
                    if yellow[yellowLoopInt] == wordArr[yellowLoopInt]:
                        wordPossible = False
                        break
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
    st.write(possibleWords)

st.title("WORDLE SOLVER")

guess1 = st.text_input("Enter your first guess (all lowercase)", "Ex: hello")   #ask for 1st guess
clues1 = st.text_input("Enter the colors of the letters in order (g = green, y = yellow, b = black)", "Ex: gybbb") #ask for clues from 1st guess

if st.button("Enter!"):
    guess1arr = list(guess1)    #convert word into an array
    clues1arr = list(clues1)    #convert clues into an array

    for i in range(5):
        if clues1arr[loopInt] == "g":
            green[loopInt] = guess1arr[loopInt]
        if clues1arr[loopInt] == "y":
            yellow[loopInt] = guess1arr[loopInt]
        if clues1arr[loopInt] == "b":
            if guess1arr not in green and guess1arr not in yellow:
                black.append(guess1arr[loopInt])
        loopInt += 1
    loopInt = 0

    checkValidWords()

guess2 = st.text_input("Enter your second guess (all lowercase)", "Ex: great")   #ask for 2nd guess
clues2 = st.text_input("Enter the colors of the letters in order (g = green, y = yellow, b = black)", "Ex: bybbb") #ask for clues from 2nd guess

if st.button("Go!"):
    guess2arr = list(guess2)    #convert word into an array
    clues2arr = list(clues2)    #convert clues into an array

    for i in range(5):
        if clues2arr[loopInt] == "g":
            green[loopInt] = guess2arr[loopInt]
        if clues2arr[loopInt] == "y":
            yellow[loopInt] = guess2arr[loopInt]
        if clues2arr[loopInt] == "b":
            if guess2arr not in green and guess2arr not in yellow:
                black.append(guess2arr[loopInt])
        loopInt += 1
    loopInt = 0

    possibleWords.clear()
    checkValidWords()

guess3 = st.text_input("Enter your third guess (all lowercase)", "Ex: crane")   #ask for 3rd guess
clues3 = st.text_input("Enter the colors of the letters in order (g = green, y = yellow, b = black)", "Ex: bbgyb") #ask for clues from 3rd guess

if st.button("Submit!"):
    guess3arr = list(guess3)    #convert word into an array
    clues3arr = list(clues3)    #convert clues into an array

    for i in range(5):
        if clues3arr[loopInt] == "g":
            green[loopInt] = guess3arr[loopInt]
        if clues3arr[loopInt] == "y":
            yellow[loopInt] = guess3arr[loopInt]
        if clues3arr[loopInt] == "b":
            if guess3arr not in green and guess3arr not in yellow:
                black.append(guess3arr[loopInt])
        loopInt += 1
    loopInt = 0

    possibleWords.clear()
    checkValidWords()

guess4 = st.text_input("Enter your fourth guess (all lowercase)", "Ex: track")   #ask for 4th guess
clues4 = st.text_input("Enter the colors of the letters in order (g = green, y = yellow, b = black)", "Ex: gyybb") #ask for clues from 4th guess

if st.button("Continue!"):
    guess4arr = list(guess4)    #convert word into an array
    clues4arr = list(clues4)    #convert clues into an array

    for i in range(5):
        if clues4arr[loopInt] == "g":
            green[loopInt] = guess4arr[loopInt]
        if clues4arr[loopInt] == "y":
            yellow[loopInt] = guess4arr[loopInt]
        if clues4arr[loopInt] == "b":
            if guess4arr not in green and guess4arr not in yellow:
                black.append(guess4arr[loopInt])
        loopInt += 1
    loopInt = 0

    possibleWords.clear()
    checkValidWords()

guess5 = st.text_input("Enter your fifth guess", "Ex: wings")   #ask for 5th guess
clues5 = st.text_input("Enter the colors of the letters in order (g = green, y = yellow, b = black)", "Ex: bgyyb") #ask for clues from 5th guess

if st.button("Return!"):
    guess5arr = list(guess5)    #convert word into an array
    clues5arr = list(clues5)    #convert clues into an array

    for i in range(5):
        if clues5arr[loopInt] == "g":
            green[loopInt] = guess5arr[loopInt]
        if clues5arr[loopInt] == "y":
            yellow[loopInt] = guess5arr[loopInt]
        if clues5arr[loopInt] == "b":
            if guess5arr not in green and guess5arr not in yellow:
                black.append(guess5arr[loopInt])
        loopInt += 1
    loopInt = 0

    possibleWords.clear()
    checkValidWords()
    st.write(green)
    st.write(black)
    st.write(yellow)
