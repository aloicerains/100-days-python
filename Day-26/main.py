# Creating the NATO alphabet

import pandas as pd

dataset = pd.read_csv('nato_phonetic_alphabet.csv')
# use for (index, row) in dataset.iterrows() to loop through each row of the data
dict_of_nato_alphabet = {row.letter: row.code for (index, row) in dataset.iterrows()}

user_input = input("Enter a word: ").upper()

# convert the user statement to corresponding NATO  alphabets
result = [dict_of_nato_alphabet.get(letter) for letter in user_input]
print(result)
