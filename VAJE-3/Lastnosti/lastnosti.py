import os
import json

file_size = os.path.getsize("C:/Users/js1262/Desktop/VAJE/VAJE3/VAJE/VAJE-3/DATA/person.json")
print(f"JSON file size: {file_size} bytes")


file_size = os.path.getsize("C:/Users/js1262/Desktop/VAJE/VAJE3/VAJE/VAJE-3/DATA/person.pb")
print(f"Protocol Buffers file size: {file_size} bytes")


#Podatkovni tipi
#JSON
with open("C:/Users/js1262/Desktop/VAJE/VAJE3/VAJE/VAJE-3/DATA/person.json", "r") as f:
    data = json.load(f)

for key, value in data.items():
    print(f"{key}: {type(value)}")

#PB
from person_pb2 import Person

person_pb = Person()

with open('C:/Users/js1262/Desktop/VAJE/VAJE3/VAJE/VAJE-3/DATA/person.pb', 'rb') as f:
    person_pb.ParseFromString(f.read())


for field, value in person_pb.ListFields():
    print(f"Field: {field.name}, Type: {field.type}, Value: {value}")