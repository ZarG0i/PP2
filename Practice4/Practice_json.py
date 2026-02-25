json_string = '{"name": "Ali", "age": 18, "isStudent": true}'
print(json_string)
#-------------------------------------
json_string = '["apple", "banana", "cherry"]'
print(json_string)
#-------------------------------------
json_string = '''
{
  "person": {
    "name": "Sara",
    "age": 20
  }
}
'''
print(json_string)
#Parsing JSON
import json

json_string = '{"name": "Alice", "age": 25, "city": "Almaty"}'
data = json.loads(json_string)
print(data)
print(type(data))
#-------------------------------------
import json

json_string = '["apple", "banana", "cherry"]'
fruits = json.loads(json_string)
print(fruits)
print(type(fruits))
#-------------------------------------
import json

json_string = '{"name": "Bob", "age": 30, "hobbies": ["reading", "gaming"]}'
person = json.loads(json_string)
print(person["hobbies"])
#-------------------------------------
import json

json_string = '{"success": true, "value": null}'
data = json.loads(json_string)
print(data)
print(type(data["success"]), type(data["value"]))
#-------------------------------------
import json

json_string = '[10, 20]'
coordinates = json.loads(json_string)
print(coordinates)
print(type(coordinates))
#Converting Python to JSON (json.dumps())
import json

data = {"name": "Alice", "age": 25, "city": "Almaty"}
json_string = json.dumps(data)
print(json_string)
#-------------------------------------
import json

fruits = ["apple", "banana", "cherry"]
json_string = json.dumps(fruits)
print(json_string)
#-------------------------------------
import json

coordinates = (10, 20)
json_string = json.dumps(coordinates)
print(json_string)
#-------------------------------------
import json

person = {"name": "Bob", "age": 30, "hobbies": ["reading", "gaming"]}
json_string = json.dumps(person, indent=4)
print(json_string)
#-------------------------------------
import json

data = {"success": True, "value": None}
json_string = json.dumps(data)
print(json_string)
#Working with JSON data

import json

with open("sample-data.json", "r") as file:
    data = json.load(file) 
print(data)
#-------------------------------------
import json

with open("sample-data.json", "r") as file:
    data = json.load(file)


user_names = [user["name"] for user in data["users"]]
print(user_names)
#-------------------------------------
import json

with open("sample-data.json", "r") as file:
    data = json.load(file)


data["users"].append({"id": 4, "name": "David", "age": 28})

with open("sample-data.json", "w") as file:
    json.dump(data, file, indent=4)  
#-------------------------------------
import json

with open("sample-data.json", "r") as file:
    data = json.load(file)

older_users = [user for user in data["users"] if user["age"] > 25]
print(older_users)
