import json

### convert dictionary to json.str

py_obj  = {
    "name" : "rohit",
    "istearch": True
}

json_str = json.dumps(py_obj)

print(type(json_str))
print(json_str)


### convert json.str to dectionary

json_str = '{"name":"rohit", "isteacher": true}'

py_obj = json.loads(json_str)

print(type(py_obj))
print(py_obj)
