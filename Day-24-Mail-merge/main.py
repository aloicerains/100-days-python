
"""
Approach:
1. Open the invited_names.txt with read permissions.
2. Real all the names and store them in a list
3. For each name in the list, open a file appended with names of the participants
4. Copy the content of the  starting letter ensuring to edit the names sections
5. Write the content into the files associated with each participant
"""
with open('Input/Letters/starting_letter.txt', 'r') as f0:
    text = f0.read()

with open('./Input/Names/invited_names.txt', 'r') as f:
    name_list = f.readlines()
    names = [name.strip() for name in name_list]
    for name in names:
        with open(f'./Output/ReadyToSend/letter_for_{name}.txt', 'w') as f1:
            new_text = text.replace("[name]", name)
            f1.write(new_text)

