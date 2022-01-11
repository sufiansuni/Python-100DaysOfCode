import pandas

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
nato_data = pandas.read_csv("day-26-NatoAlphabet/nato_phonetic_alphabet.csv")
nato_dict = {row["letter"]:row["code"] for (index, row) in nato_data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    word = input("Enter a word:")
    try:
        decoded = [nato_dict[letter.upper()] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(decoded)

generate_phonetic()
