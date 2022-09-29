"""
python token.py xxx.json
"""
import json
import sys
  
# Opening JSON file
f = open(sys.argv[1])
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Iterating through the json
# list
for i in data['tokens']:
    print(i['token'])
  
# Closing file
f.close()