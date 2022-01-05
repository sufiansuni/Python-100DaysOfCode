with open("day-26-ListComprehension/file1.txt") as file_one:
    file_one_data = [ line.strip() for line in file_one]

with open("day-26-ListComprehension/file2.txt") as file_two:
    file_two_data = [ line.strip() for line in file_two]

result = [num for num in file_one_data if num in file_two_data]

# Write your code above 👆

print(result)
