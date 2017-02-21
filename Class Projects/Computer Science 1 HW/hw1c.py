#Carter Cahill
#A02
#00962727

x = float(input("Input a real number: "))
t = int(input("Input a nonnegative integer: "))

series = 1
counter = 1
while counter <= t:
    value = ((x ** counter)/counter)
    series = series + value
    counter = counter + 1
print(series)