with open("day7/input.txt") as file:
    lines = [line.strip() for line in file]

beams = {i for i, ch in enumerate(lines[0]) if ch == "S"}
count = 0
for line in lines[1:]:
    splitters = {i for i, ch in enumerate(line) if ch == "^"}
    encounters = splitters & beams
    count += len(encounters)
    beams -= splitters
    for enc in list(encounters):
        left = enc - 1
        right = enc + 1
        beams.update({left,right})
print(count)