instructions = []
nodes = {}

with open("Input.txt", "r") as file:
    instructions = file.readline().strip()

    for line in file:
        line = line.strip()
        if line == "":
            continue

        node, nexts = line.split(" = ")
        nexts = nexts[1:-1].split(", ")

        nodes[node] = nexts

current = "AAA"
ins = 0
steps = 0
while current != "ZZZ":
    if instructions[ins] == "L":
        current = nodes[current][0]
    else:
        current = nodes[current][1]

    ins = (ins + 1) % len(instructions)
    steps += 1

print(steps)
