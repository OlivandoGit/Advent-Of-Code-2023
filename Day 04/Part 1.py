cards = {}
total = 0

with open("Input.txt", "r") as file:
    for line in file:
        line = line[line.index(":") + 1:]
        line = line.strip().split(" ")

        winning = [int(x) for x in line[:line.index("|")] if x != ""]
        numbers = [int(x) for x in line[line.index("|") + 1 :] if x != ""]

        points = -1
        for num in numbers:
            if num in winning:
                points += 1

        if points != -1:
            total += 2 ** points

print(total)
