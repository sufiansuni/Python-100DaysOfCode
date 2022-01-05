import pandas

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
nato_data = pandas.read_csv("day-26-NatoAlphabet/nato_phonetic_alphabet.csv")
nato_dict = {row["letter"]:row["code"] for (index, row) in nato_data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word:")
decoded = [nato_dict[letter.upper()] for letter in word if letter.upper() in nato_dict]
print(decoded)
