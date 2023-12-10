from math import lcm

instructions = []
nodes = {}

with open("test.txt", "r") as file:
    instructions = file.readline().strip()

    for line in file:
        line = line.strip()
        if line == "":
            continue

        node, nexts = line.split(" = ")
        nexts = nexts[1:-1].split(", ")

        nodes[node] = nexts

starts = [node for node in nodes if node[-1] == "A"]

stepsFinal = []

for start in starts:
    current = start

    ins = 0
    steps = 0
    while current[-1] != "Z":
        if instructions[ins] == "L":
            current = nodes[current][0]
        else:
            current = nodes[current][1]

        ins = (ins + 1) % len(instructions)
        steps += 1

    stepsFinal.append(steps)

print(lcm(*stepsFinal))
