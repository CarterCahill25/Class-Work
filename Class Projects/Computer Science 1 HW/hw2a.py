#Carter Cahill
#A02
#00962727

range1 = "[0, 25]   " #set the ranges for the test grades
range2 = "(25, 50]  "
range3 = "(50, 75]  "
range4 = "(75, 100] "
done = False #set done as false so it exits the while loop when done
while done != True:
    score = (input("Enter test score: "))#ask for input of test grades
    if score == "Done": #set up way to close loop if enter "Done"
        done = True
    else:#Put "*" in range that it fits in
        score = int(score)
        if 0 <= score <= 25:
            range1 = range1 + "*"
        elif 25 < score <= 50:
            range2 = range2 + "*"
        elif 50 < score <= 75:
            range3 = range3 + "*"
        elif 75 < score <= 100:
            range4 = range4 + "*"
#print ranges and *'s
print(range1)
print(range2)
print(range3)
print(range4)
        