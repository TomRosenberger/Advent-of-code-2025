with open("day7/input.txt") as file:
    lines = [line.strip() for line in file]

beams = {i:1 for i, ch in enumerate(lines[0]) if ch == "S"}
count = 0

for line in lines[2:-1:2]:
    splitters = {i for i, ch in enumerate(line) if ch == "^"}
    encounters = splitters & set(beams.keys())
    for enc in list(encounters):
        left = enc - 1
        right = enc + 1
        beams[left] = beams.get(left, 0) + beams[enc]
        beams[right] = beams.get(right, 0) + beams[enc]
        beams.pop(enc)

print(sum(beams.values()))