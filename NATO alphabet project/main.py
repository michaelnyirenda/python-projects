import pandas as p

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data = p.read_csv("nato_phonetic_alphabet.csv")
nato = p.DataFrame(data)
nato_dict = {row.letter:row.code for (index, row) in nato.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
nato_code_words = [nato_dict[letter] for letter in word]
print(nato_code_words)