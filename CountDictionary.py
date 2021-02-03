#Neah Garza
#MIS 4322
#Dictionary Exercise 1

def update_input(data):
        data = data.replace('"', '')
        data = data.replace('.', '')
        #data = data.replace("'", "")
        data = data.replace("‘", "")
        #data = data.replace("’", "")
        data = data.replace("-", " ")
        data = data.replace(",", "")
        #data = data.replace("_", "")
        data = data.replace('“', '')
        data = data.replace('”', '')
        return data

def createDictionary(words, dictionary):
    for index in words:
        if index in dictionary:
            dictionary[index] = dictionary[index] + 1
        else:
            dictionary[index] = 1

def main():
    infile = open("text.txt", "r")
    check = infile.readline()

    if(not check):
        print("Error! Nothing in file")
    else:
        text = infile.read()
        text = update_input(text)
        input = text.split()
        myDictionary = {}
        createDictionary(input, myDictionary)

    infile.close()
    print("WORD : FREQUENCY\n")
    for key,value in myDictionary.items():
        print(key, ":", value)

main()