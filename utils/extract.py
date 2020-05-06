import csv
import json

tweets = []
#sf = open('tweet.json', 'r')
with open('tweet.json') as f:
    data = [json.loads(line) for line in f]
for line in d.items():
    print(line)
    #tweets.append(json.loads(line))
