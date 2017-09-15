# working with dictionary in Python v.3.5.2
# there is a .json file with several pairs word/explanation
# the user ask to the program a word to explain it.

import json
from difflib import get_close_matches

data = json.load(open("data.json", 'r'))


def voc(word):
    guess = get_close_matches(word, data.keys())[0]
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        c = input("Did you meant %s instead?" % guess + " press y/n: ")
        if c == "y":
            return data[guess]
        else:
            return "The word doesn't exist. Please double check it!"
    else:
        return "The word doesn't exist. Please double check it!"


word = input("Enter word: ").lower()

print(voc(word))
