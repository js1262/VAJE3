import json

person = {
    "name" : "Alice",
    "age" : 30,
    "address": {
        "street" : "dunajska",
        "city" : "Ljubljana"
    },
    "married" : True
}

with open('C:/Users/js1262/Desktop/VAJE/VAJE3/VAJE/VAJE-3/DATA/person.json', 'w') as f:
    json.dump(person, f, indent=4, sort_keys=True)