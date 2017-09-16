# working with dictionary in Python v.3.5.2
# given the data.json file with several pairs word/explanation
# the user ask to the program a word to explain it.

import json
from difflib import get_close_matches

data = json.load(open("data.json", 'r'))


def voc(w):
    lst = get_close_matches(w, data.keys(), cutoff=0.8)
    if w in data:
        return data[w]
    elif len(lst) > 0:
        c = input("Did you mean %s instead?" % lst[0] + " press y/n: ")
        while len(c) > 1 or c.lower() != "y" and c.lower() != "n":
            c = input("Your entry is invalid. Please enter the letter 'y' for 'yes' or 'n' for 'no': "
            ).lower()
        if c == "y":
            return data[lst[0]]
        elif c == "n":
            dic = dict(enumerate(lst, start=1))
            print(dic)
            try:
                d = int(input("Which word did you want to translate?\nPlease, enter the number corresponded to the word: "))
                if d in dic:
                    return data[dic[d]]
                else:
                    return "The number you're entering isn't correct."
            except ValueError as error:
                print(error)

        else:
            return "The word doesn't exist. Please double check it!"
    else:
        return "The word doesn't exist. Please double check it!"


while True:
    word = input("Enter word ('q' for quit): ").lower()
    if word == "q":
        print("See you again!")
        break
    else:
        result = voc(word)
        if type(result) == list:
            count = 0
            for i in result:
                count += 1
                print(str(count) + ". " + i)
        else:
            print(voc(word))
