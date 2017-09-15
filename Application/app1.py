# working with dictionary in Python v.3.5.2
# given the data.json file with several pairs word/explanation
# the user ask to the program a word to explain it.

import json
from difflib import get_close_matches

data = json.load(open("data.json", 'r'))

def voc(w):
    lst = get_close_matches(w, data.keys())
    if w in data:
        return data[w]
    elif len(lst) > 0:
        c = input("Did you mean %s instead?" % lst[0] + " press y/n: ")
        if c == "y":
            return data[lst[0]]
        elif c == "n":
            return "The word doesn't exist. Please double check it!"
        else:
            return "Sorry, we didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it!"


word = input("Enter word: ").lower()

print(voc(word))
