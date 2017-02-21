import math
n= 1 #set a place holder for N
N = int(input("Enter postive number:")) #ask user for barrier number
while n <= N:
    n2 = n + 1 #set n2 to 1 more than n
    while n2 <= N:
        z = (n*n) + (n2*n2)#take the n and n2 and find their z
        z = math.sqrt(z)#take square root of it
        if z % 1 == 0:#if z % 1 == 0 then it must be an integer
            print(n,n2,int(z)) #prints the ones that work
        n2 = n2 + 1 #add 1 to n2
    n = n + 1#add 1 to n