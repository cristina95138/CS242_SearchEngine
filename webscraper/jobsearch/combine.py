import json

files=['indeed.json', 'indeed.json']

def merge_JSON(filename):
    result = list()
    for f1 in filename:
        with open(f1, 'r') as infile:
            result.extend(json.load(infile))

    with open('indeed_combined.json', 'w') as output_file:
        json.dump(result, output_file)

# merge_JsonFiles(files)