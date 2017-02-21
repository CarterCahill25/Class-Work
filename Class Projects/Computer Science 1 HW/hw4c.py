#Carter Cahill
#A02
#00962727

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