import json

with open("data.json", "r") as file:
    data = json.load(file)


def translate(word):
    return data.get(word, "word not found")


word = input("enter word : ").lower()

print(translate(word))
