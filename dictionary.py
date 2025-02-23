import json

with open("data.json", "r") as file:
    data = json.load(file)


def translate(word):
    return data[word]


word = input("enter word : ")

print(translate(word))
