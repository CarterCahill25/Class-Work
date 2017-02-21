#Carter Cahill
#A02
#00962727

def parse(s):
    s = s + " " #add a space to the end of the string
    s = s.lower() #lowercase all letters in string
    s = [s] #make s a list
    index = 0
    word = ""
    processing = False #set processing to false to start off
    newList = []
    while index < len(s[0]): #while s is smaller than s's length
        S = (s[0][index]) #save S as the element at that index
        if "a" <= S <= "z": #to check if a symbol is a letter
            processing = True #if so start processing
            word = word + str(s[0][index])
        else: #if not a letter
            if processing: #and you are processing a word
                if len(word) >= 4: #check if it a long enough word
                    Word = [(word)]
                    newList = newList + (Word) # add word to the list of words
                    processing = False #no longer processing a word
                word = ""
        index = index + 1
    return(newList)

def computeWordFrequencies(filename):
    f = open(filename)
    line = f.readline() #read first line
    lineW = []
    listWords = []
    finalWords = []
    WordCounter = []
    index = 0
    while line != "": #read lines until you read ""
        lineW = parse(line) #use parse function
        listWords.extend(lineW) #extend ListWords with new found words in the line
        line = f.readline() #read the next line
    listWords = sorted(listWords)
    while index < len(listWords):
        word = listWords[index]
        if not (listWords[index] in finalWords): #if this word at index is not in finalWords append it and append 1 to WordCounter
            finalWords.append(word)
            WordCounter.append(1)
        elif (listWords[index] in finalWords): #if it is then add 1 to its counter
            n = finalWords.index(word)
            WordCounter[n] = WordCounter[n] + 1
        index = index + 1
    return(finalWords, WordCounter)
    
def mostFrequentWords(wordList, frequencyList, k):
    FrequentWords = []
    FrequentIndex = []
    length = len(wordList) #take length of wordList
    placementOfLargest = 0 
    largest = 0
    counter = 0
    lastLargest = 999999999999999 #start lastLargest at huge number
    while counter < k:
        index = 0
        while index < length: #while index is less then length
            if frequencyList[index] > largest and frequencyList[index] < lastLargest: #check in frequency number is large than current largest but less then last largest
                largest = frequencyList[index] #if so this number is new largest
                placementOfLargest = index
            index = index + 1
        lastLargest = largest #this largest is now lastLargest
        counter = counter + 1
        largest = 0
        FrequentWords.append(wordList[placementOfLargest]) #append word to list
        FrequentIndex.append(frequencyList[placementOfLargest]) #append its frequency
    return(FrequentWords,FrequentIndex)

print("Tolstoy")
(wordList, frequencyList) = computeWordFrequencies("war.txt") #run war.txt
(T, number) = mostFrequentWords(wordList, frequencyList, 20)
print(T)

index = 0
#first produce both list for hyde and treasure
(wordList1, frequencyList1) = computeWordFrequencies("hyde.txt")
(wordList2, frequencyList2) = computeWordFrequencies("treasure.txt")
while index < len(wordList2) - 1: #combine both list
    if wordList2[index] in wordList1:
        n = wordList1.index(wordList2[index])
        frequencyList1[n] = frequencyList1[n] + frequencyList2[index]
    else:
        wordList1.append(wordList2[index])
        frequencyList1.append(frequencyList2[index])
    index = index + 1
#run this new made lists
print("R.L.Stevenson")
(RL, numberList) = mostFrequentWords(wordList1, frequencyList1, 20)
print(RL)

