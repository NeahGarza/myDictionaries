#Neah Garza
#MIS 4322
#Dictionary Exercise 2

def addWinner(winners, dictionary):
    if winners in dictionary:
        dictionary[winners] = dictionary[winners] + 1
    else:
        dictionary[winners] = 1

def addYear(year, dictionary, winner):
    dictionary[year] = winner
    return (year + 1)

def main():
    infile = open("WorldSeriesWinners.txt", "r")
    check = infile.readline()
    addFirst = False
    startYear = 1903
    currentYear = -1
    #Following list represent years games weren't played
    skipYears = ["1904", "1994"]
    skipLen = len(skipYears)-1

    if(not check):
        print("Error! Nothing in file")
    else:
        if(not addFirst):
            #Adding the first line read from file to dictinoary
            check = check.rstrip()
            winnersDict = {}
            yearsDict = {}
            addWinner(check, winnersDict)
            currentYear = startYear
            currentYear = addYear(currentYear, yearsDict, check)
            addFirst = True
        for line in infile:
            #Adding the rest of items to dictionaries
            if:
            else:
                line = line.rstrip()
                addWinner(line, winnersDict)
                currentYear = addYear(currentYear, yearsDict, check)

    infile.close()
    
    keepGoing = True
    while(keepGoing):
        whichYear = int(input("Please enter a year (between 1903 - 2008): "))
        print("The winner for year", whichYear, "was the:", yearsDict[whichYear])
        print("This team has won the World Series", winnersDict[yearsDict[whichYear]], "times")

        flag = str(input("\nWould you like to see the winner for another year? (Y = yes, anything else = no): "))
        flag = flag.upper()
        if(flag not "Y"):
            keepGoing = False

main()