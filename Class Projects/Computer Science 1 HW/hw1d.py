#Carter Cahill
#A02
#00962727

S = float(input("Enter a postive S: "))
E = float(input("Enter a postive E: "))
G = float(input("Enter a guess: "))
aDif = 0
while E > aDif:
    D = S/(G)
    if D > G:
        aDif = (D + G)/ 2
    elif G > D:
        aDif = (G + D)/ 2
    G = aDif
print(aDif)