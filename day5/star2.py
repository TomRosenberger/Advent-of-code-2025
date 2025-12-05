with open("day5/input.txt") as file:
    content = file.read().strip()

ranges_block, ids_block = content.split("\n\n")
ranges = [[int(r) for r in line.strip().split("-")] for line in ranges_block.split("\n")]

connected_ranges = []
for range in ranges:
    start, end = range
    if connected_ranges:
        pop_indices = []
        for i, exist_range in enumerate(connected_ranges[:]):
            exist_start,exist_end = exist_range
            if exist_start <= start <= exist_end or exist_start <= end <= exist_end or (start <= exist_start and end >= exist_end):
                connected_ranges[i][0] = min(start,exist_start)
                connected_ranges[i][1] = max(end, exist_end)
                start,end= connected_ranges[i]
                pop_indices.append(i)
        if len(pop_indices) == 0:
            connected_ranges.append(range)
        if len(pop_indices) > 1:
            for indice in reversed(pop_indices[:-1]):
                connected_ranges.pop(indice)
    else:
        connected_ranges.append(range)

print(sum([range[1]-range[0]+1 for range in connected_ranges]))