from math import sqrt
# distance = wurzel von (x1-x2)²+(y1-y2)²+(z1-z2)²
with open("day8/input.txt") as file:
    lines = [[int(i) for i in line.split(",")] for line in file]

length = len(lines)

def calc_all_dist():
    distances = {}
    for line in range(length): 
        for line2 in range(line+1,length):
            distance = sqrt(((lines[line][0]-lines[line2][0])**2) + ((lines[line][1]-lines[line2][1])**2) + ((lines[line][2]-lines[line2][2])**2))
            distances[(line,line2)] = distance
    sorted_distances = sorted(distances.items(), key= lambda item: item[1])
    return sorted_distances

def get_connected_junctions(sorted_distances):
    connected_junctions= []
    for d in sorted_distances[:length]:
        connected_junctions.append(set(d[0]))
    return connected_junctions

def merge_junctions(c_junctions):
    merged = []
    for j in c_junctions:
        overlapping = [m for m in merged if not j.isdisjoint(m)]
        for m in overlapping:
            j |= m
            merged.remove(m)
        merged.append(j)
    return merged

sorted_distances = calc_all_dist()
connected_junctions = get_connected_junctions(sorted_distances) 
merged = merge_junctions(connected_junctions)

output = 1

for j in sorted(merged,key=len,reverse=True)[:3]:
    output *= len(j)

print(output)