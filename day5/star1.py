with open("day5/input.txt") as file:
    content = file.read().strip()

ranges_block, ids_block = content.split("\n\n")
ranges = [[int(r) for r in line.strip().split("-")] for line in ranges_block.split("\n")]
ids = [int(line.strip()) for line in ids_block.split("\n")]

count = 0
for id in ids:
    for range in ranges:
        start, end = range
        if start <= id <= end:
            count += 1
            break

print(count)