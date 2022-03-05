from pathlib import Path
import streamlit as st

p = Path(__file__).with_name('words.txt')
f = open(p, "r")       

green = ['', '', '', '', '']    
yellow = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']  
black = []      
possibleWords = []

loopInt = 0

allWordsArray = []
for wordInFile in f:
    newWord = wordInFile.replace("\n", "")
    allWordsArray.append(newWord)

f.close()

def checkValidWords():
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
                    elif yellow[yellowLoopInt+5] != '' and yellow[yellowLoopInt+5] == wordArr[yellowLoopInt]:
                        wordPossible = False
                        break
                    elif yellow[yellowLoopInt+10] != '' and yellow[yellowLoopInt+10] == wordArr[yellowLoopInt]:
                        wordPossible = False
                        break
                    elif yellow[yellowLoopInt+15] != '' and yellow[yellowLoopInt+15] == wordArr[yellowLoopInt]:
                        wordPossible = False
                        break
                    elif yellow[yellowLoopInt+20] != '' and yellow[yellowLoopInt+20] == wordArr[yellowLoopInt]:
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

guess1 = st.text_input("Enter your first guess (all lowercase)", "Ex: hello")  
clues1 = st.text_input("Enter the colors of the letters in order (g = green, y = yellow, b = black)", "Ex: gybbb")

if st.checkbox("Enter!"):
    guess1arr = list(guess1)   
    clues1arr = list(clues1)   

    for i in range(5):
        if clues1arr[loopInt] == "g":
            green[loopInt] = guess1arr[loopInt]
        if clues1arr[loopInt] == "y":
            yellow[loopInt] = guess1arr[loopInt]
        if clues1arr[loopInt] == "b":
            if guess1arr[loopInt] not in green and guess1arr[loopInt] not in yellow:
                black.append(guess1arr[loopInt])
        loopInt += 1
    loopInt = 0

    checkValidWords()

guess2 = st.text_input("Enter your second guess (all lowercase)", "Ex: great")   
clues2 = st.text_input("Enter the colors of the letters in order (g = green, y = yellow, b = black)", "Ex: bybbb")

if st.checkbox("Go!"):
    guess2arr = list(guess2)    
    clues2arr = list(clues2)   
    for i in range(5):
        if clues2arr[loopInt] == "g":
            green[loopInt] = guess2arr[loopInt]
        if clues2arr[loopInt] == "y":
            yellow[loopInt+5] = guess2arr[loopInt]
        if clues2arr[loopInt] == "b":
            if guess2arr[loopInt] not in green and guess2arr[loopInt] not in yellow:
                black.append(guess2arr[loopInt])
        loopInt += 1
    loopInt = 0

    possibleWords.clear()
    checkValidWords()

guess3 = st.text_input("Enter your third guess (all lowercase)", "Ex: crane")  
clues3 = st.text_input("Enter the colors of the letters in order (g = green, y = yellow, b = black)", "Ex: bbgyb") 

if st.checkbox("Submit!"):
    guess3arr = list(guess3)   
    clues3arr = list(clues3)  

    for i in range(5):
        if clues3arr[loopInt] == "g":
            green[loopInt] = guess3arr[loopInt]
        if clues3arr[loopInt] == "y":
            yellow[loopInt+10] = guess3arr[loopInt]
        if clues3arr[loopInt] == "b":
            if guess3arr[loopInt] not in green and guess3arr[loopInt] not in yellow:
                black.append(guess3arr[loopInt])
        loopInt += 1
    loopInt = 0

    possibleWords.clear()
    checkValidWords()

guess4 = st.text_input("Enter your fourth guess (all lowercase)", "Ex: track")   
clues4 = st.text_input("Enter the colors of the letters in order (g = green, y = yellow, b = black)", "Ex: gyybb") 

if st.checkbox("Continue!"):
    guess4arr = list(guess4)    
    clues4arr = list(clues4)    

    for i in range(5):
        if clues4arr[loopInt] == "g":
            green[loopInt] = guess4arr[loopInt]
        if clues4arr[loopInt] == "y":
            yellow[loopInt+15] = guess4arr[loopInt]
        if clues4arr[loopInt] == "b":
            if guess4arr[loopInt] not in green and guess4arr[loopInt] not in yellow:
                black.append(guess4arr[loopInt])
        loopInt += 1
    loopInt = 0

    possibleWords.clear()
    checkValidWords()

guess5 = st.text_input("Enter your fifth guess", "Ex: wings")   
clues5 = st.text_input("Enter the colors of the letters in order (g = green, y = yellow, b = black)", "Ex: bgyyb") 

if st.checkbox("Return!"):
    guess5arr = list(guess5)    
    clues5arr = list(clues5)    

    for i in range(5):
        if clues5arr[loopInt] == "g":
            green[loopInt] = guess5arr[loopInt]
        if clues5arr[loopInt] == "y":
            yellow[loopInt+20] = guess5arr[loopInt]
        if clues5arr[loopInt] == "b":
            if guess5arr[loopInt] not in green and guess5arr not in yellow:
                black.append(guess5arr[loopInt])
        loopInt += 1
    loopInt = 0

    possibleWords.clear()
    checkValidWords()
