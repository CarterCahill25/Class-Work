#Carter Cahill
#A02
#00962727

import math

N = int(input("Please type a positive integer: "))
N1 = -1 #put place holder 
n = 2 # n will take on values from 2 through N and we will test each n for primality
while n <= N:
    factor = 2 # initial value of possible factor
    isPrime = True # variable to remember if n is a prime or not
    factorUpperBound = math.sqrt(n) # the largest possible factor we need to test is sqrt(n)

    # loop to generate and test all possible factors
    while (factor <= factorUpperBound):
        # test if n is evenly divisible by factor
        if (n % factor == 0):
            isPrime = False
            break
    
        factor = factor + 1
    
    # Output 
    if isPrime:
        if n - 2 == N1:#if the previous prime is 2 away
            print(N1,n) #print previous prime and current
        N1 = n #set current prime as old prim
        


    n = n + 1