# Import non-standard modules
import json


def definition(word):
    '''This function returns the available definitions(s) of the input'''
    return data[word]


# Load dictionary data from data.json to python dictionary
data = json.load(open('data.json', 'r'))


while True:
    ip = input("Enter word:")
    if ip in {'!q', '!Q'}:
        break
    elif data.__contains__(ip):
        print(definition(ip))
    else:
        print("Please enter a valid word! \nEnter '!q' to quit!!!\n")
