#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("day-24-MailMerge/Input/Letters/starting_letter.txt", mode="r") as starting_letter_file:
    starting_letter = starting_letter_file.read()


with open("day-24-MailMerge/Input/Names/invited_names.txt", mode="r") as names_file:
    invited_names = names_file.readlines()

for name in invited_names:
    proper_name = name.strip()
    custom_letter = starting_letter.replace("[name]", proper_name)
    with open(f"day-24-MailMerge/Output/ReadyToSend/letter_for_{proper_name}.txt", mode="w") as new_file:
        new_file.write(custom_letter)
