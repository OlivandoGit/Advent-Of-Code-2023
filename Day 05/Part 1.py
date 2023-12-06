def inRange(r, num):
    mapRange = range(int(r[1]), int(r[1]) + int(r[2]))

    if num in mapRange:
        return int(r[0]) + (num - int(r[1]))

    return -1


seeds = []
maps = []

with open("Input.txt", "r") as file:
    seeds = file.readline()
    seeds = [int(x) for x in seeds.strip().split(": ")[1].split(" ")]

    tempMaps = []
    for line in file:
        line = line.strip()
        if line == "":
            maps.append(tempMaps)
            tempMaps = []

        else:
            tempMaps.append(line.split(" "))

    maps.append(tempMaps)

maps = maps[1:]
maps = [m[1:] for m in maps]

locations = []
for seed in seeds:
    current = seed
    for map in maps:
        for r in map:
            mapped = inRange(r, current)
            if mapped != -1:
                current = mapped
                break

    locations.append(current)

print(min(locations))
