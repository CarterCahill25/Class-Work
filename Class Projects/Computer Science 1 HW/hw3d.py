import random
def twoDRandomWalk(n = 100, printOn = True):
    counter = 0
    y = 0
    x = 0
    while abs(y) < n and abs(x) < n: #while x and y are less than n 
        step = random.randint(1,4)#generate 4 numbers to represent north, east, south, and west
        if step == 1: #step north
            y = y + 1
        if step == 2: #step south
            y = y - 1
        if step == 3: #step east
            x = x + 1
        if step == 4: #step west
            x = x - 1
        counter = counter + 1 #increment counter after each step
        if printOn == True: #if printOn is true then print after each step
            print(x,y)
    return(counter)
            