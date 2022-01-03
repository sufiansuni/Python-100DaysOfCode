# Modes
# r = read
# w = write
# a = append

with open("day-24-FilesDirectoriesPaths/my_file.txt", mode="w") as file:
    file.write("New Text.")

with open("day-24-FilesDirectoriesPaths/my_file.txt") as file:
    contents = file.read()
    print(contents)
