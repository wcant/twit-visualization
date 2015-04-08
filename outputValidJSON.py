import json
import csv
#from pymongo import MongoClient

#Establish db connection
#client = MongoClient()
#db = client.twitter
#collection = db.stream_2day

# Text file with one tweet per line
DATA_FILE = 'custom_range.json'

def jsonStreamParse(DATA_FILE):
    # Build JSON array
    data = "{0}".format(",".join([l for l in open(DATA_FILE).readlines()]))
    split = data.split('\n,')

    # Convert list of strings into list of dicts
    print("Converting data string to list of dictionaries...")
    data = [json.loads(line) for line in split]

    print("Extracting coordinates...")
    coordinates = [data[i]["coordinates"] for i in range(len(data))]
    time_stamp = [data[i]["created_at"] for i in range(len(data))]

    # Count point types
    point_count = 0
    null_count = 0

    for i in coordinates:
        try:
            if (i["type"] == "Point"):
                point_count+=1
        except TypeError:
            null_count+=1
            continue
    print("%d Point types found." % (point_count))
    print("%d Nulls found." % (null_count))

    return coordinates, time_stamp, point_count, null_count

# Generate output for plotting
coordinates, time_stamp, point_count, null_count = jsonStreamParse(DATA_FILE)
outputDict = {}
iKey = 0
for l in zip(coordinates, time_stamp):
    try:
        outputDict[str(iKey)] = {
                              "coordinates":l[0]["coordinates"],
                              "timestamp":l[1]
                             }
    except TypeError:
        outputDict[str(iKey)] = None
        continue
    iKey+=1

# Output json file
with open('data.json', 'w') as outfile:
    json.dump(outputDict, outfile)

# Output csv file
with open('data.csv', 'wb') as outfile:
    writer = csv.writer(outfile, delimiter=',')
    for key in outputDict:
        writer.writerow(outputDict[key]["coordinates"])
