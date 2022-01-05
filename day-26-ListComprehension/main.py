numbers = [1,2,3]
# new_list = []
# for n in numbers:
#     new_item = n + 1
#     new_list.append(new_item)
# print(new_list)

# new_list = [n + 1 for n in numbers]
# print(new_list)

word = input("Enter a word:")

new_list = [char.upper() for char in word if char.isalpha()]
print(new_list)
