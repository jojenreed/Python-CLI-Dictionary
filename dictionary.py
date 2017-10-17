# Import non-standard modules
import json
from difflib import get_close_matches


def definition(word):
    '''This function returns the available definitions(s) of the input'''
    return data[word]


# Load dictionary data from data.json to python dictionary
data = json.load(open('data.json', 'r'))

# Infinite loop for processing
while True:
    # Accept case-insensitive input from user
    ip = str(input("Enter word:")).lower()
    # Exit from program - user choice
    if ip == '!q':
        break
    # Check dictionary for definition
    elif data.__contains__(ip):
        print(definition(ip))
    # If exact definition is not found, provide suggestion
    elif len(get_close_matches(ip, data.keys(), cutoff=0.8)) > 0:
        print("Did you mean to type",
              get_close_matches(ip, data.keys(), cutoff=0.8)[0], "?(y/n):")
        choice = str(input()).lower()
        # Provide output if generated suggestion is accepted
        if choice == 'y':
            ip = get_close_matches(ip, data.keys(), cutoff=0.8)[0]
            print(definition(ip))
    # No suggestion or definition found
    else:
        print("No such word exists!! \nEnter '!q' to quit!!!")
