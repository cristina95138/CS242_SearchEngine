import json

filename = 'part-r-00000'

mainDict = {}
j = 0

with open(filename) as fh:
    for line in fh:
        row = list(line.strip().split(None, -1))
        tempDict = {}

        tempDict["token"] = row[0]
        for i in range(1, len(row)):
            docCountPair = row[i].split(':')
            page = docCountPair[0].split('.')
            tempDict[page[0]] = docCountPair[1]
        
        mainDict[j] = tempDict
        j = j + 1

output_file = open("mapReduceCount.json", "w")
json.dump(mainDict, output_file, indent = 4)
output_file.close()



