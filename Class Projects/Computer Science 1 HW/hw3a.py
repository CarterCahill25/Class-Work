#Carter Cahill
#A02
#00962727
import math
def isPrime(x):

    factor = 2 # initial value of possible factor
    isPrime = True # variable to remember if n is a prime or not
    factorUpperBound = math.sqrt(x) # the largest possible factor we need to test is sqrt(n)
    
    # loop to generate and test all possible factors
    while (factor <= factorUpperBound) and (isPrime):
        # test if n is evenly divisible by factor
        if (x % factor == 0):
            isPrime = False
        
        factor = factor + 1 #test next factor
        
    return(isPrime)#return if it prime in form of boolean

def farthestConsecutivePrimes(N):
    x = 1
    second = 1
    greatest = 0
    while x <= N: #this will test number up to N
        t = isPrime(x) #run the number through isPrime function
        if t == True: #if isPrime returns True then save it as first
            first = x
            diff = first - second #find the difference by taking this new number - the last found prime
            if diff > greatest: #if this new difference is greater then the previous greatest 
                greatest = diff #save this new difference as greatest
                m = second #and save first and second as new primes
                n = first
            second = first #save new prime as the old
        x = x + 1 #check next number
    print([m,n]) #print final answer