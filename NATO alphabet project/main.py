import pandas as p


# {"A": "Alfa", "B": "Bravo"}
data = p.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in data.iterrows()}

while True:
    word = input("Enter a word: ").upper()
    try: 
        nato_code_words = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        continue
    else:
        break
print(nato_code_words)