#write a code that will open a file and give a test in the form the file is in
def adminQuiz(filename):
    file = open(filename)#open the file
    numberA = file.readline()#read the first line in the file and save as number of answers
    numberQ = file.readline()#read the second line in the file and save as number of questions
    numberA = (int(numberA))#make number of answers a interger
    numberQ = (int(numberQ))#make number of questions a intergers
    correctCounter = 0#set correct counter to 0
    x = 0#set varible x to 0
    y = 0#set varible y to 0
    while x < (numberQ): #while x less then number of questions
        z = 1 # set z to 1
        question = file.readline() #read line for the question
        question = str(question) #ask the question in the form of a string    
        while y < (numberA): #while y is less than number of answers  
            answers = file.readline() #read line and sign as answers
            answers = (str(z) + ". " + (answers)) #save answer number z and answer
            print(answers)#print answer
            y = y + 1 #add 1 to y
            z = z + 1 #add 1 to z
        print(question.strip()) #print striped question
        print("***RESPOND WITH THE NUMBER THAT CORRESPONDS WITH THE ANSWERS***")#give instructions on how to answer questions
        answer = input("Enter Answer:") #ask user for answers
        x = x + 1 #add 1 to x
        actual = file.readline() #readline and set to actual 
        actual = (actual).strip() #strip actual and set to actual
        if str(answer) == str(actual): #if str(answer) = str(actual)
            print("Correct!") #print "Correct!"
            correctCounter = correctCounter + 1 #add to 1 to counter
        elif str(answer) != str(actual): # elif str(answer) != str(actual)
            print("Sorry you are wrong") # print "Sorry you are wrong"
        y = 0 #set y = 0
    percent = (correctCounter/numberQ) #percent = correctCounter divided numberQ
    percent = (percent)*100 #save percent as percent * 100
    file.close() # close file
    if correctCounter == 1:
        if numberQ == 1:
            return("You answered " + str(correctCounter) + " question correctly out of " + str(numberQ) + " question. Awesome job!!")
        else:
            if 89<(percent)<101:
                return("You answered " + str(correctCounter) + " question correctly out of " + str(numberQ) + " questions. Awesome job!!")
            elif 74<(percent)<90:
                return("You answered " + str(correctCounter) + " question correctly out of " + str(numberQ) + " questions. Great job!")
            elif 59<(percent)<75:
                return("You answered " + str(correctCounter) + " question correctly out of " + str(numberQ) + " questions. Good job!")
            elif 44<(percent)<60:
                return("You answered " + str(correctCounter) + " question correctly out of " + str(numberQ) + " questions. You did average!")
            elif 0<(percent)<45:
                return("You answered " + str(correctCounter) + " question correctly out of " + str(numberQ) + " questions. You didn't do too good!")
    else:
        if 89<(percent)<101:
            return("You answered " + str(correctCounter) + " questions correctly out of " + str(numberQ) + " questions. Awesome job!!")
        elif 74<(percent)<90:
            return("You answered " + str(correctCounter) + " questions correctly out of " + str(numberQ) + " questions. Great job!")
        elif 59<(percent)<75:
            return("You answered " + str(correctCounter) + " questions correctly out of " + str(numberQ) + " questions. Good job!")
        elif 44<(percent)<60:
            return("You answered " + str(correctCounter) + " questions correctly out of " + str(numberQ) + " questions. You did average!")
        elif 0<(percent)<45:
            return("You answered " + str(correctCounter) + " questions correctly out of " + str(numberQ) + " questions. You didn't do too good!")                   