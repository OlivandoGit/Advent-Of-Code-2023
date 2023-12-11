image = []

with open("Input.txt", "r") as file:
    image = [list(line.strip()) for line in file]

emptyRows = [y for y, row in enumerate(image) if "#" not in row]
empltyCols = [x2 for x2, col in enumerate([[image[y][x] for y in range(len(image))] for x in range(len(image[0]))]) if "#" not in col]

galaxies = [(x + (999_999 * len([c for c in empltyCols if c < x])), y + (999_999 * len([r for r in emptyRows if r < y]))) for y, row in enumerate(image) for x, chr in enumerate(row) if chr == "#"]

pairs = [(a, b) for i, a in enumerate(galaxies) for b in galaxies[i + 1:]]

paths = [abs(y2 - y1) + abs(x2 - x1) for ((x1, y1), (x2, y2)) in pairs]

print(sum(paths))
