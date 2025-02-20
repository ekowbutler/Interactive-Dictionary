import json

with open("data.json", "r") as file:
    data = json.load(file)

print(data)

input("\nPress Enter ot exit...")
