"""
curl -XGET \
"http://localhost:9200/upload_history/_analyze?filter_path=tokens.token" \
-H 'Content-Type: application/json' \
-d '{  "analyzer" : "custom_analyzer",  "text": "_test@TEST_11/*&^/%$#_"}' | python token_std_normal.py

curl -XGET \
"http://localhost:9200/upload_history/_analyze?filter_path=tokens.token" \
-H 'Content-Type: application/json' \
-d '{  "analyzer" : "custom_analyzer",  "text": "_test@TEST_11/*&^/%$#_"}'
"""
import json
import sys

data = json.load(sys.stdin)
for i in data['tokens']:
    print(i['token'])