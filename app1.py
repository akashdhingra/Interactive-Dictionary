import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data.keys():
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif len(get_close_matches(w,data.keys()))>0:
        yn = input("Do you mean %s instead? Press y for yes and n for no: " % get_close_matches(w,data.keys())[0])
        if yn=="y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == "n":
            return "The word does not exist. Please enter the correct word"
        else:
            return "Wrong input"
    else:
        return "The word does not exist. Please enter the correct word"

word = input("Enter any word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
