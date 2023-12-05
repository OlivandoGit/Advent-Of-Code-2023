total = 0

with open("Input.txt", "r") as file:
    for line in file:
        mins = {"red" : 0, "green" : 0, "blue" : 0}

        line = line.strip()
        gameID, subsets = line.split(": ")

        gameID = int(gameID.split(" ")[1])

        subsets = subsets.split("; ")
        subsets = [subset.split(", ") for subset in subsets]

        for sub in subsets:
            for cubes in sub:
                num, colour = cubes.split(" ")
                num = int(num)

                if num > mins[colour]:
                    mins[colour] = num

        minProduct = 1
        for min in mins.values():
            minProduct *= min

        total += minProduct

print(total)
