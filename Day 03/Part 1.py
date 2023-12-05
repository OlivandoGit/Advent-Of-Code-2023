total = 0

with open("Input.txt", "r") as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]


    for y, line in enumerate(lines):
        x = 0
        while x < len(line):
            char = line[x]

            if not char.isdigit():
                x += 1
                continue

            x2 = x
            while(x2 < len(line) and line[x2].isdigit()):
                x2 += 1

            x3 = x - 1
            valid = False
            for i in range(x2 - x):
                x3 += 1
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if dy == 0 and dx == 0:
                            continue

                        if y + dy in range(0, len(lines)):
                            if x3 + dx in range(0, len(line)):
                                if not lines[y + dy][x3 + dx].isalnum() and lines[y + dy][x3 + dx] != ".":
                                    valid = True

            if valid:
                total += int(line[x:x2])


            x = x2


print(total)
