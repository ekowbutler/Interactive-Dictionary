import json
from difflib import get_close_matches

with open("data.json", "r") as file:
    data = json.load(file)


def translate(word):
    if word in data:
        return data.get(word)
    elif len(get_close_matches(word, data.keys())) > 0:
        user_decision = input(
            f"did you mean {get_close_matches(word,data.keys())[0]} instead? Enter Y if Yes or N if No: "
        )
        if user_decision == ("Y").lower():
            return data[get_close_matches(word, data.keys())[0]]
        elif user_decision == ("N").lower():
            return (word, ": word not found")


word = input("enter word : ").lower()

print(translate(word))
