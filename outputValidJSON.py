import json

# text file with one tweet per line
DATA_FILE = 'custom_range.json'

# build JSON array
data = "{0}".format(",".join([l for l in open(DATA_FILE).readlines()]))
split = data.split('\n,')

# Convert list of strings into list of dicts
data = [json.loads(split[i]) for i in range(1000)]
