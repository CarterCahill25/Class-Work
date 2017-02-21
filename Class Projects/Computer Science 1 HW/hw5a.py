#Carter Cahill
#A02
#0096272
import time

# Two words are neighbors if they differ in exactly on letter.
# This function returns True if a given pair of words are neighbors
def areNeighbors(w1, w2):
    count = 0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            count = count + 1
    
    return count == 1

# The function reads from the file "words.dat" and inserts the words that are read
# into a list. The words are also inserted into a dictionary as keys, with each key 
# initialized to have [] as its value.
def readWords(wordList, D):
    
    fin = open("words.dat", "r")

    # Loop to read words from the and to insert them in a list
    # and in a dictionary
    for word in fin:
        newWord = word.strip("\n")
        wordList.append(newWord)
        wordMatrix[1].append([(newWord[1:]), newWord[0]])
        firstLetter = newWord[0]
        letterIndex = ord(firstLetter) - 97
        wordMatrix[0][letterIndex].append(newWord)
        D[newWord] = []
    fin.close()
    

# Builds the network of words using a dictionary. Two words are connected by an edge in this
# network if they are neighbors of each other, i.e., if they differ from each
# other in exactly one letter.
def buildDictionary(wordList, D):
    for word in wordList:
        Start = ord(word[0]) - 97
        for item in wordMatrix[0][Start]:
            if areNeighbors(word, item):
                D[word].append(item)
        for thing in wordMatrix[1]:
            if thing[0] == word[1:]:
                Word = thing[1] + thing[0] 
                D[word].append(Word)
    
    
# Explores the network of words D starting at the source word. If the exploration ends
# without reaching the target word, then there is no path between the source and the target.
# In this case the function returns False. Otherwise, there is a path and the function
# returns True.
def searchWordNetwork(source, target, D):

    # Initialization: processed and reached are two dictionaries that will help in the 
    # exploration. 
    # reached: contains all words that have been reached but not processed.
    # processed: contains all words that have been reached and processed, i.e., their neighbors have also been explored.
    # The values of keys are not useful at this stage of the program and so we use 0 as dummy values.
    processed = {source:0}
    reached = {}
    for e in D[source]:
        reached[e] = 0
       
    # Repeat until reached set becomes empty or target is reached 
    while reached:
        # Check if target is in reached; this would imply there is path from source to target
        if target in reached:
            return True
        
        # Pick an item in reached and process it
        item = reached.popitem() # returns an arbitrary key-value pair as a tuple
        newWord = item[0]
        
        # Find all neighbors of this item and add new neighbors to reached
        processed[newWord] = 0
        for neighbor in D[newWord]:
            if neighbor not in reached and neighbor not in processed:
                reached[neighbor] = 0 
    
    return False
        
# Main program
wordList = []
D = {}
wordMatrix = [[], []]
counter = 0 
while counter < 27:
    wordMatrix[0].append([])
    counter = counter + 1
    
readWords(wordList, D)
buildDictionary(wordList, D)

source = input("Please type the source word: ")
target = input("Please type the target word: ")

if searchWordNetwork(source, target, D):
    print("There is path from source to target")
else:
    print("There is no path from source to target")