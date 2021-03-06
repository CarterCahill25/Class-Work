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
    result = {}
    f = open(filename)
    line = f.readline() #read first line
    lineW = []
    listWords = []
    while line != "": #read lines until you read ""
        lineW = parse(line) #use parse function
        listWords.extend(lineW) #extend ListWords with new found words in the line
        line = f.readline() #read the next line
    listWords = sorted(listWords)
    for item in listWords:
        if item not in result:
            result[item] = 1
        else:
            result[item] = result[item] + 1
            
    return(result)  
    
   