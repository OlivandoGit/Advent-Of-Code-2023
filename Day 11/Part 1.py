image = []

with open("Input.txt", "r") as file:
    image = [list(line.strip()) for line in file]

rows = [y for y, row in enumerate(image) if "#" not in row]
cols = [x2 for x2, col in enumerate([[image[y][x] for y in range(len(image))] for x in range(len(image[0]))]) if "#" not in col]

for i, r in enumerate(rows):
    image.insert(r + i, ["." for i in range(len(image[0]))])

for i, c in enumerate(cols):
    for row in image:
        row.insert(c + i, ".")

galaxies = [(x, y) for y, row in enumerate(image) for x, chr in enumerate(row) if chr == "#"]

pairs = [(a, b) for i, a in enumerate(galaxies) for b in galaxies[i + 1:]]

paths = [abs(y2 - y1) + abs(x2 - x1) for ((x1, y1), (x2, y2)) in pairs]

print(sum(paths))
