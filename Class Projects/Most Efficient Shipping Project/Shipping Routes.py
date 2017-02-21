#Carter Cahill
#A02
#00962727

###############################################################################
#Phase 1
def createDataStructure():
    file = open("miles.dat")#open miles file
    line = file.readline()#read first line
    cities = [] #start cities, coordinates, population, and distances as empty list
    coordinates = []
    population = []
    distances = []
    cityName= "" #start them as empty strings
    Cords = ""
    Pop = ""
    distance = ""
    processingCity = False
    processingCord = False
    processingPop = False
    counter = -1 #start counter at -1 so it become 0 when it reads first line
    for line in file:
        if "A" <= line[0] <= "Z":#check if it is a city line
            counter = counter + 1 #add 1 to counter 
            coordinates.append([])#append a empty list to coordinates and distances
            distances.append([])
            distances[counter].append(0)#also append a 0 this citys distance list
            distanceCounter = counter #set distanceCounter and counter to the same thing
            for element in line:#read each element in line
                if "A" <= element <= "Z" or "a" <= element <= "z" or element == " " or element == "-":
                    #check if element is any characters included in city names
                    processingCity = True#then start processing the city
                    cityName = cityName + element#add characters to cities name
                if processingCity:#if processing City name
                    if element == ",":#"," turns processing false
                        processingCity = False
                    if element == "[":#ends processing of city 
                        cities.append(cityName)#append current cityName to cities list
                        cityName = ""# reset cityName to ""
                        processingCord = True#start processing Cord (coordinates)
                if processingCord:
                    if "0" <= element <= "9": #if it reads a number
                        Cords = Cords + element #add number to Cord being processed
                    if element == ",": #if "," then done reading long
                        Cords = int(Cords)
                        coordinates[counter].append(Cords)#append Cord to empty list at index of the city
                        Cords = ""
                    if element == "]":
                        processingCord = False
                        Cords = int(Cords)
                        coordinates[counter].append(Cords)
                        Cords = ""
                        processingPop = True
                if processingPop:
                    if "0" <= element <= "9":
                        Pop = Pop + element
                    if element ==  "\n":
                        Pop = int(Pop)
                        population.append(Pop)
                        Pop = ""
                        processingPop = False
        if "0" < line[0] <= "9":
            for element in line:
                if "0" <= element <= "9":
                    distance = distance + element
                if not "0" <= element <= "9":
                    distance = int(distance)
                    distances[distanceCounter-1].append(distance)
                    distances[counter].insert(0, distance)
                    distance = ""
                    distanceCounter = distanceCounter - 1
    data = [cities, coordinates, population, distances]
    return(data)

def getCoordinates(city, data):
    index = data[0].index(city)
    cord = data[1][index]
    return(cord)

def getPopulation(city, data):
    index = data[0].index(city)
    pop = data[2][index]
    return(pop)

def getDistance(firstCity, secondCity, data):
    index1 = data[0].index(firstCity)
    index2 = data[0].index(secondCity)
    distance = data[3][index1][index2]
    return(distance)

def nearbyCities(City, Range, data):
    index = data[0].index(City)
    List = data[3][index]
    counter = 0
    finalList = []
    for element in List:
        if element <= Range:
            finalList.append(data[0][counter])
        counter = counter + 1
    finalList.sort()
    return finalList
###################################################################
#PHASE2
def locateFacilities(data, r):
    unserved = [(data[0]), (data[3]), (["Y"] * 128)]
    wantedList = ["N"] *128
    currentHigh = 0
    counter = 0
    Count = 1
    finalList = []
    servedList = []
    while unserved[2] != wantedList:
        for city in unserved[0]:
            counter = 0
            index = (unserved[0]).index(city)
            index = int(index)
            for element in unserved[0]:
                elementIndex = unserved[0].index(element)
                distance = unserved[1][index][elementIndex]
                if distance <= r and unserved[2][elementIndex] == "Y":
                    counter = counter + 1
                    servedList.append(unserved[0][elementIndex])
            if counter > currentHigh:
                highCity = city
                servedListFinal = servedList
                currentHigh = counter
            servedList = []
        finalList.append(highCity)
        cityIndex = unserved[0].index(highCity)
        unserved[2][cityIndex] = "N"
        for item in servedListFinal:
            servedCityIndex = data[0].index(item)
            unserved[2][servedCityIndex] = "N"
        currentHigh = 0
    finalList.sort()
    return(finalList)

###################################################################
#Phase 3
data = createDataStructure()
facilities = locateFacilities( data, 800)
def display(facilities, data):
    file = open("visualization800.kml", "w")
    file.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
    file.write('  <Document>\n')
    file.write('    <Style id="smalline">\n')
    file.write('      <LineStyle>\n')
    file.write('        <color>7f00007f</color>\n')
    file.write('        <width>7</width>\n')
    file.write('      </LineStyle>\n')
    file.write('      <PolyStyle>\n')
    file.write('        <color>7f00007f</color>\n')
    file.write('      </PolyStyle>\n')
    file.write('    </Style>\n')
    for city in facilities:
        file.write('    <Placemark>\n')
        file.write('      <name>' + (city) + '</name>\n')
        file.write('      <description>' + (city) + '</description>\n')
        file.write('      <Point>\n')
        index = data[0].index(city)
        cords = data[1][index]
        L1 = str(cords[0])
        lent = len(L1)
        lent = lent - 2
        L1 = (L1[:(lent)] + "." + L1[(lent):])
        L2 = str(cords[1])
        lent = len(L2)
        lent = lent - 2
        L2 = (L2[:(lent)] + "." + L2[(lent):])
        file.write('        <coordinates>-' + str(L2) + ',' + (L1) + ',0,</coordinates>\n')
        file.write('      </Point>\n')
        file.write('    </Placemark>\n')
    for city in data[0]:
        if city not in facilities:
            closeRange = 9999999999999999999999
            index = data[0].index(city)
            for element in data[3][index]:
                elementIndex = (data[3][index]).index(element)
                if element < closeRange and (data[0][elementIndex]) in facilities:
                    closeRange = element
                    nearestFac = elementIndex
            file.write('    <Placemark>\n')
            file.write('      <name>' + (city) + " - " + (data[0][nearestFac]) + '</name>\n')
            file.write('      <description>' + ('Path from ' + (city) + ' to ' + (data[0][nearestFac])) + '</description>\n')
            file.write('      <styleUrl>#smallline</styleUrl>\n')        
            file.write('      <LineString>\n')
            file.write('        <extrude>1</extrude>\n')
            file.write('        <tessellate>1</tessellate>\n')
            file.write('        <alitudeMode>absolute</alitudeMode>\n')
            file.write('        <coordinates>\n')
            index = data[0].index(city)
            cords = data[1][index]
            L1 = str(cords[0])
            lent = len(L1)
            lent = lent - 2
            L1 = (L1[:(lent)] + '.' + L1[(lent):])
            L2 = str(cords[1])
            lent = len(L2)
            lent = lent - 2
            L2 = (L2[:(lent)] + '.' + L2[(lent):])        
            file.write('          -' + str(L2) + ',' + str(L1) + ',0 ')
            cords = data[1][nearestFac]
            L1 = str(cords[0])
            lent = len(L1)
            lent = lent - 2
            L1 = (L1[:(lent)] + "." + L1[(lent):])
            L2 = str(cords[1])
            lent = len(L2)
            lent = lent - 2
            L2 = (L2[:(lent)] + '.' + L2[(lent):])   
            file.write('-' + str(L2) + ',' + str(L1) + ',0\n')
            file.write('        </coordinates>\n')
            file.write('      </LineString>\n')
            file.write('    </Placemark>\n')
    file.write('  </Document>\n')
    file.write('</kml>')
    file.close()