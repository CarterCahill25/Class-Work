import random
def thinkNumber():
    #use a bool to determine if we need to prompt the user for a number
    needAGuess = True
    #need random whole number 1 through 10
    myNumber = random.randint(1,10)
    myString = "I am thinking of a whole number between 1 and 10. Guess it:"
    while (needAGuess):
    #prompt the user for their guess
        userGuess = input(myString)
        if (myNumber == int(userGuess)):
    #if guess is correct, return a string with the message
            return "Yes, You guessed it!"
            #if the guess is incorrect, prompt the user for another guess
        else:
            myString = ("Wrong answer. Guess again:")

    