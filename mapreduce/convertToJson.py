import json

filename = 'part-r-00000'

mainDict = {}

with open(filename) as fh:
    for line in fh:
        row = list(line.strip().split(None, -1))
        tempDict = {}

        for i in range(1, len(row)):
            docCountPair = row[i].split(':')
            tempDict[docCountPair[0]] = docCountPair[1]
        
        mainDict[row[0]] = tempDict

output_file = open("mapReduceCount.json", "w")
json.dump(mainDict, output_file, indent = 4)
output_file.close()



