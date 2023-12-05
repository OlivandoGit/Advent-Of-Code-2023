allowed = {"red" : 12, "green" : 13, "blue" : 14}
total = 0

with open("Input.txt", "r") as file:
    for line in file:
        line = line.strip()
        gameID, subsets = line.split(": ")

        gameID = int(gameID.split(" ")[1])

        subsets = subsets.split("; ")
        subsets = [subset.split(", ") for subset in subsets]

        valid = True
        for sub in subsets:
            for cubes in sub:
                num, colour = cubes.split(" ")
                num = int(num)

                if num > allowed[colour]:
                    valid = False

        if valid:
            total += gameID

print(total)
