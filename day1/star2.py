with open("day1/input.txt") as file:
    rotations = [rotation.strip() for rotation in file]

number = 50
count = 0
for r in rotations:
    n = int(r[1:])
    if r[0] == "R":
        for _ in range(n):
            number += 1
            if number % 100 == 0:
                count += 1
    else:
        for _ in range(n):
            number -= 1
            if number % 100 == 0:
                count += 1
print(count)