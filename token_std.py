"""
curl -XGET \
"http://localhost:9200/upload_history/_analyze" \
-H 'Content-Type: application/json' \
-d '{  "analyzer" : "custom_analyzer",  "text": "_test@TEST_11/*&^/%$#_"}' | python token_std.py


curl -XGET \
"http://localhost:9200/upload_history/_analyze" \
-H 'Content-Type: application/json' \
-d '{  "analyzer" : "custom_analyzer",  "text": "_test@TEST_11/*&^/%$#_"}'
"""
import json
import sys

data = json.load(sys.stdin)
list = ''
for i in data['tokens']:
    offset = i['end_offset'] - i['start_offset']
    if offset == 1:
        print(list)
        list = ''
    list = list + i['token'] + ','