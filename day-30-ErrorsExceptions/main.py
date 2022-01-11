# FileNotFound
# with open("something.txt") as file:
#     file.read()

# KeyError
# dictionary = {"key": "value"}
# value = dictionary["keynoexist"]

# IndexError
# list = [1, 2, 3]
# value = list[3]

# try: something that might cause an exception
# except: do this if there was an exception
# else: do this if there was NO exception
# finally: do this no matter what happens

# try:
#     file = open("day-30-ErrorsExceptions/data.txt")
#     dictionary = {"key": "value"}
#     value = dictionary["key"]
# except FileNotFoundError:
#     # print("There was an error")
#     file = open("day-30-ErrorsExceptions/data.txt", "a")
# except KeyError as error_msg:
#     print(f"The key {error_msg} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File Closed")

def calc_bmi(weight, height):
    if height > 3:
        raise ValueError("Humans should not go over 3 meters in height")
    bmi = weight / height **2
    return bmi

height = float(input("Height: "))
weight = int(input("Weight: "))
bmi = calc_bmi(weight, height)
