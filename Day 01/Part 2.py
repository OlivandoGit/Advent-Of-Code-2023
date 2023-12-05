def getFirst(line, strs):
    for index, char in enumerate(line):
        if char.isdigit():
            return char

        for num, st in enumerate(strs):
            if char != st[0]:
                continue

            if "".join(line[index : index + len(st)]) == st:
                return str(num + 1)

    return "False"


strs = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
total = 0

with open("Input.txt", "r") as file:
    for line in file:
        line = list(line.strip())

        numbers = [getFirst(line, strs), getFirst(line[::-1], [st[::-1] for st in strs])]

        numbers = list(filter(lambda chr: chr.isdigit(), numbers))

        total += int(numbers[0] + numbers[-1])

print(total)
