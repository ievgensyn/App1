# working with dictionary in Python v.3.5.2
# given the data.json file with several pairs word/explanation
# the user ask to the program a word to explain it.

import json
from difflib import get_close_matches

data = json.load(open("data.json", 'r'))


def voc(w):
    guess = get_close_matches(w, data.keys())[0]
    if w in data:
        return data[w]
    elif len(get_close_matches(word, data.keys())) > 0:
        c = input("Did you mean %s instead?" % guess + " press y/n: ")
        if c == "y":
            return data[guess]
        else:
            return "The word doesn't exist. Please double check it!"
    else:
        return "The word doesn't exist. Please double check it!"


word = input("Enter word: ").lower()

print(voc(word))
