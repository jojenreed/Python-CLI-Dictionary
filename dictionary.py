# Import non-standard modules
import json
from difflib import get_close_matches


def definition(word):
    '''This function returns the available definitions(s) of the input'''
    for i in data[word]:
        print(i)
    return("")


# Load dictionary data from data.json to python dictionary
data = json.load(open('data.json', 'r'))

# Infinite loop for processing
while True:
    # Accept case-insensitive input from user
    ip = str(input("Enter word:(!q to quit)  ")).lower()
    # Exit from program - user choice
    if ip == '!q':
        break
    # Check dictionary for definition
    elif data.__contains__(ip):
        print(definition(ip))
    # Check dictionary for definition of input as a proper noun
    elif data.__contains__(ip[0].upper() + ip[1:]):
        print(definition(ip[0].upper() + ip[1:]))
    # If exact word is not found, provide a suggestion
    elif len(get_close_matches(ip, data.keys(), cutoff=0.8)) > 0:
        print("Did you mean to type",
              get_close_matches(ip, data.keys(), cutoff=0.8)[0], "?(y/n):")
        choice = str(input()).lower()
        # Provide output if suggested word is accepted by user
        if choice == 'y':
            ip = get_close_matches(ip, data.keys(), cutoff=0.8)[0]
            print(definition(ip))
        elif choice == 'n':
            print("Try again with the corrected spelling or press !q to quit")
        else:
            print()
    # If no definition or suggestion was found
    else:
        print("No such word exists!! \nEnter '!q' to quit!!!")
