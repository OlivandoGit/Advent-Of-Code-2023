northValid = ["|", "7", "F", "S"]
eastValid = ["-", "7", "J", "S"]
southValid = ["|", "L", "J", "S"]
westValid = ["-", "L", "F", "S"]

tiles = []
with open("Input.txt", "r") as file:
    tiles = [[p for p in line.strip()] for line in file]

coords = (0, 0)
for y, row in enumerate(tiles):
    for x, t in enumerate(row):
        if t == "S":
            coords = (x, y)
            break

path = ["S"]
last = ""
while len(path) == 1 or path[-1] !=  "S":
    if coords[1] - 1 >= 0 and tiles[coords[1] - 1][coords[0]] in northValid and path[-1] in southValid and last != "SOUTH":
        coords = (coords[0], coords[1] - 1)
        last = "NORTH"

    elif coords[0] + 1 < len(tiles[0]) and tiles[coords[1]][coords[0] + 1] in eastValid and path[-1] in westValid and last != "WEST":
        coords = (coords[0] + 1, coords[1])
        last = "EAST"

    elif coords[1] + 1 < len(tiles) and tiles[coords[1] + 1][coords[0]] in southValid and path[-1] in northValid and last != "NORTH":
        coords = (coords[0], coords[1] + 1)
        last = "SOUTH"

    elif coords[0] - 1 >= 0 and tiles[coords[1]][coords[0] - 1] in westValid and path[-1] in eastValid and last != "EAST":
        coords = (coords[0] - 1, coords[1])
        last = "WEST"

    path.append(tiles[coords[1]][coords[0]])

print((len(path) - 1) // 2)
