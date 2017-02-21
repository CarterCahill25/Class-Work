import math

def nearHalfInteger(f):
    x = math.trunc(f)#truncate the given number and saw as x
    x = f - x#subtract the given number by x
    x = abs(x)#take absolute value of x
    if .499 <= x <= .501: #if x falls between .499 and .501 then it is a half integer
        s = math.trunc(f)#truncate the given function
        if f < 0:
            f = s - .5#if a negative number substract .5
            return(f)
        f = s + .5 #if postive add .5
        return(f)
    if .999 <= x <= 1: #if x is in given range it means its a half integer
        if f < 0:
            return math.floor(f)#round down
        f = math.ceil(f) #round up
        return(f)
    if 0 <= x <= .001:
        if f < 0:
            return math.ceil(f) #round up      
        f = math.floor(f) #round down
        return(f)
    return None #if it doesnt fit any then it is none