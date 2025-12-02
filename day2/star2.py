ranges = []
with open("input.txt") as file:
        ranges = file.readline().split(",")

invalids = set()
for r in ranges:
    i1,i2 = (r.split("-"))
    for i in range(int(i1), int(i2)+1):
        i = str(i)
        possible_slices = []
        for x in range(2,len(i)+1):
            if len(i) % x == 0:
                possible_slices.append(len(i) // x)       
        for slice in possible_slices:
            parts = []
            multi = 1
            end = 0
            while end < len(i):
                start = slice * (multi-1)
                end = slice * multi
                part = i[start:end]
                parts.append(part)
                multi += 1
            if len(set(parts)) == 1:
                invalids.add(int(i))

print(sum(invalids))