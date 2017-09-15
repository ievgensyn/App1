# working with dictionary in Python v.3.5.2
# there is a .json file with several pairs word/explanation
# the user ask to the program a word to explain it.

import json

data = json.load(open("data.json", 'r'))


def voc(word):
    if word in data:
        return data[word]
    else:
        return "The word doesn't exist. Please double check it!"


word = input("Enter word: ").lower()

print(voc(word))
