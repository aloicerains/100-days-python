# Creating the NATO alphabet

import pandas as pd

dataset = pd.read_csv('nato_phonetic_alphabet.csv')
# use for (index, row) in dataset.iterrows() to loop through each row of the data
dict_of_nato_alphabet = {row.letter: row.code for (index, row) in dataset.iterrows()}


def nato_alphabet():
    """Functions Validates user input and prints the alphabets"""
    user_input = input("Enter a word: ").upper()

    # convert the user statement to corresponding NATO  alphabets
    # result = [dict_of_nato_alphabet.get(letter) for letter in user_input]
    # I do not want to print None for non-existing characters hence us try block

    try:
        result = [dict_of_nato_alphabet[letter] for letter in user_input]
    except KeyError:
        print('Sorry! Only letters in the alphabet please!')
        # As long as users keep on entering numbers, they will be given new text prompt
        nato_alphabet()
    else:
        print(result)


nato_alphabet()


