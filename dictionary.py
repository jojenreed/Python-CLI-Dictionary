# Import non-standard modules
import json
from difflib import get_close_matches


def definition(word):
    '''This function returns the available definitions(s) of the input'''
    if data.__contains__(word):
        return(data[word])
    elif data.__contains__(word.lower()):
        return(data[word.lower()])
    # Generate suggestions for user
    elif len(get_close_matches(word, data.keys(), cutoff=0.8)) > 0:
        choice = input("Did you mean to type %s ?(y/n):"
                       % get_close_matches(word, data.keys(), cutoff=0.8)[0])
        choice = choice.lower()
        if choice == 'y':
            ip = get_close_matches(word, data.keys(), cutoff=0.8)[0]
            return(data[ip])
        elif choice == 'n':
            return("Please try again with the correct spelling")
        else:
            return("Invalid input!")
    else:
        return("Could not find a similar word!!")


# Load dictionary data from data.json to python dictionary
data = json.load(open('data.json', 'r'))

# Infinite loop for processing
while True:
    ip = input("Enter word:(!q to quit)  ")
    # Exit from program - user choice
    if ip == '!q' or ip == '!Q':
        break
    else:
        # Check dictionary for definition
        output = definition(ip)
        if type(output) == list:
            for i in output:
                print(i)
        else:
            print(output)
