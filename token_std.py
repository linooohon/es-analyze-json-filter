"""
curl -XGET \
"http://localhost:9200/upload_history/_analyze" \
-H 'Content-Type: application/json' \
-d '{  "analyzer" : "custom_analyzer",  "text": "_test@TEST_11/*&^/%$#_"}' | python token_std.py
"""
import json
import sys

data = json.load(sys.stdin)
for i in data['tokens']:
    print(i['token'])