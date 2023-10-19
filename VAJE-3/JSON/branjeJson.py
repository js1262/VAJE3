import json

with open('C:/Users/js1262/Desktop/VAJE/VAJE3/VAJE/VAJE-3/DATA/person.json', 'r') as f:
    deserialized_person = json.load(f)

    deserialized_person['age'] = 40
    deserialized_person['married'] = False

with open('C:/Users/js1262/Desktop/VAJE/VAJE3/VAJE/VAJE-3/DATA/personUpdated.json', 'w') as f:
    json.dump(deserialized_person, f, indent=4)