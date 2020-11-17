# A program to convert Bibfiles
# into csv, json and jaml

def main():
    # create a dictonary
    import re
    dictionary = {
    "recodType": "recordType",
    "citationKey": "citationKey",
    "title": "tile",
    "author": "author",
    "year": "date",
    "date": "date",
    "location": "location"
    }
    
    #read in the file
    fname= input("Enter a filename: ")
    infile = open(fname, "r", encoding="utf8")
    data = infile.read()
     # now split it
    myList = data.split("\n@")
    # from here on it goes wrong
    # loop through the record to split again
    for i in range(len(myList)):
        element = myList[i].split(",\n")
        firstEntry = element[0].split("{")
        recordType = firstEntry[0].strip()
        citationKey = firstEntry[1].strip()
        myList["recordType"] = recordType
        myList["citationkey"] = citationKey
        # split key values
        for x in range(1, len(element), 1):
            key, value = element[x].split("=")
         
            dictionary[element] = key, value
    print(dictionary)
main()


