import json

# ## for load data

with open("JSON_Methods//data.json", "r") as f :
    py_obj = json.load(f)
    print(py_obj)
    print(type(py_obj))


### dump data

data  = {
    "name" : "Rohit",
    "age" : 27,
    "isTearcher" : True
}

with open("JSON_Methods//data.json", "w") as f :
    json.dump(data, f)  # with use indent = 4