ranges = []
with open("input.txt") as file:
        ranges = file.readline().split(",")

invalids = 0
for r in ranges:
    i1,i2 = (r.split("-"))
    if len(i1) + len(i2) % 2 == 0:
        continue
    else:
        for i in range(int(i1), int(i2)+1):
            i = str(i)
            if len(i) % 2 != 0:
                continue
            else:
                mid = len(i) // 2
                left = i[:mid]
                right = i[mid:]
                if left == right:
                    invalids += int(i)
print(invalids)             