```
curl -X GET \
"localhost:9200/upload_history/_analyze?pretty" \
-H 'Content-Type: application/json' \
-d \
'{
  "analyzer" : "custom_analyzer",
  "text" : "-1 test test -1 ---- 1 -- @@ __ _ --"
}' \
| python token_std_normal.py
```