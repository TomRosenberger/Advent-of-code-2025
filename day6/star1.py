from math import prod

with open("day6/input.txt") as file:
    content = file.read().split("\n")
    numbers= [[int(n) for n in line.split()] for line in content[:-1]]
    operations = [operation for operation in content[-1].split()]

hash_map = {}
line_length = len(numbers[0])

for line_index, line in enumerate(numbers):
    for number_index in range(line_length):
        hash_map.setdefault(number_index, []).append(numbers[line_index][number_index])

output = 0

for operator in range(line_length):
    current_numbers = hash_map[operator]
    if operations[operator] == "+":
        output += sum(current_numbers)
    else:
        output += prod(current_numbers)

print(output)


