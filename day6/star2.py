from math import prod

with open("day6/input.txt") as file:
    content = file.read().split("\n")
    numbers= [line for line in content[:-1]]
    operations = [operation for operation in content[-1]]

starting_incices = [i for i, o in enumerate(operations) if o != " "]
matrix = []

for i, start in enumerate(starting_incices):
    column = []
    for line in numbers:
        if i < len(starting_incices)-1:
            number = line[start:starting_incices[i+1]-1]
        else:
            number = line[start:]
        column.append([n for n in number])
    matrix.append(column)

output = 0
for i, column in enumerate(matrix):
    operator = operations[starting_incices[i]]
    len_col = len(column[0])
    calc = []
    for place in range(len_col):
        number_str = ""
        for n in column:
            number_str += n[place]
        calc.append(int(number_str))
    if operator == "*":
        output += prod(calc)
    else:
        output += sum(calc)

print(output)