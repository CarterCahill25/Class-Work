import math

def nearHalfInteger(f):
    x = math.trunc(f)
    x = f - x
    x = abs(x)
    if .499 <= x <= .501:
        s = math.trunc(f)
        if f < 0:
            f = s - .5
            return(f)
        f = s + .5
        return(f)
    if .999 <= x <= 1:
        if f < 0:
            return math.floor(f)
        f = math.ceil(f)
        return(f)
    if 0 <= x <= .001:
        if f < 0:
            return math.ceil(f)        
        f = math.floor(f)
        return(f)
    return None

n = input("Enter a postive integer: ")
times = 0
counter = 0
while times < int(n):
    h = input("")
    a = nearHalfInteger(float(h))
    print(a)
    if a != None:
        counter = counter + 1
    times = times + 1
print("The number of near half integers is " + str(counter))