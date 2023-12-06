seedRanges = []
unparsedMaps = []

with open("test.txt", "r") as file:
    seedRanges = file.readline()
    seedRanges = [int(x) for x in seedRanges.strip().split(": ")[1].split(" ")]

    tempMaps = []
    for line in file:
        line = line.strip()
        if line == "":
            unparsedMaps.append(tempMaps)
            tempMaps = []

        else:
            tempMaps.append(line.split(" "))

    unparsedMaps.append(tempMaps)

unparsedMaps = unparsedMaps[1:]
unparsedMaps = [m[1:] for m in unparsedMaps]

maps = [[[int(x) for x in m] for m in mapLayer] for mapLayer in unparsedMaps]

seeds = [(x, x + d - 1) for x, d in zip(seedRanges[::2], seedRanges[1::2])]

for mapLayer in maps:
    newSeeds = []
    while len(seeds) > 0:
        seedStart, seedEnd = seeds.pop()
        for m in mapLayer:
            rangeOutput, rangeStart, rangeDelta = m

            rangeEnd = rangeStart + rangeDelta - 1

            if rangeStart <= seedStart <= seedEnd <= rangeEnd:
                newSeeds.append((seedStart - rangeStart + rangeOutput, seedEnd - rangeStart + rangeOutput))
                break

            if rangeStart <= seedStart <= rangeEnd < seedEnd:
                seeds.extend([(seedStart, rangeEnd), (rangeEnd + 1, seedEnd)])
                break

        else:
            newSeeds.append((seedStart, seedEnd))

    seeds = newSeeds

print(min(min(seeds)))
