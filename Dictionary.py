r"""
This program is designed to translate and define word

This program suppose to help those who dont understand kiswahili(swahili) and

Those who need to know definition of some word in english.

User search English word and program translate the word in Kiswahili(swahili) and
give example of that word.

I Expert anyone fix the bug found and extend the program in you language
"""
import json
from difflib import get_close_matches

data = json.load(open("data.json", "r"))


def English_definition(word):
    word = word.lower()
    if word in data:
        # try:
        return data[word]
    # except KeyError:
    elif word.title() in data:
        return data[word.title()]  # In case user search for word start with capital latter eg.English
    elif word.upper() in data:
        return data[word.upper()]  # In case user search for acronyms word eg NATO,NACTE
    elif len(get_close_matches(word, data.keys())) > 0:

        Answer = input("\nDid you mean %s  ? Yes/No " % get_close_matches(word, data.keys())[0])
        Answer = Answer.lower()
        if Answer == "yes":
            return data[get_close_matches(word, data.keys())[0]]

        elif Answer == "no":
            print("See you again!Later\n")
            choice_menu(choice)

        else:
            return "We didn't understand your entry!"

    else:
        return "The word doesn't not exist,Please double check"


def Swahili_dictionary(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        choice_menu(choice)


def choice_menu(choice):
    print("_-_-_--Language Dictionary--_--__--\n")
    print("1 English Word And Definition\n2 Swahili Word And Definition\n3 Translation Swahili to English\n\n4 Quit")
    choice = int(input("\nSelect one of the choice: "))
    while choice < 5:

        if choice == 1:
            print("\n_-_-_--English Word And Definition--_--__--\n")
            word = input("\nEnter word: ")

            display = English_definition(word)

            if type(display) == list:

                for item in display:
                    print(item)
            else:
                print(display)
        elif choice == 2:
            print("\n_-_-_--Swahili Word And Definition--_--__--\n")
            word = input("\nWeka neno la Kiswahili: ")
            Swahili_dictionary(word)
            choice_menu(choice)
            break
        elif choice == 3:
            print("Under Construction!!")
            choice_menu(choice)
        elif choice == 4:
            print("Goodbye !!")
            break
        else:
            print("Wrong Choice you May try Again")
            choice_menu(choice)


choice = 0
choice_menu(choice)
