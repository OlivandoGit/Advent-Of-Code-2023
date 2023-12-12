def arrange(row, groups):
    row = row.lstrip(".")

    if row == "":
        return int(len(groups) == 0)

    if len(groups) == 0:
        return int(row.find("#") == -1)

    if row[0] == "#":
        ##Not enough row left or . in first group length
        if len(row) < groups[0] or "." in row[:groups[0]]:
            return 0

        ##Row is same length as first group
        elif len(row) == groups[0]:
            return int(len(groups) == 1)

        ##Invalid no gap between groups
        elif row[groups[0]] == "#":
            return 0

        else:
            return arrange(row[groups[0] + 1:], groups[1:])

    return arrange("#" + row[1:], groups) + arrange(row[1:], groups)

rows = []

with open("Input.txt", "r") as file:
    rows += [(line.strip().split()[0], [int(x) for x in line.strip().split()[1].split(",")]) for line in file]

print(sum([arrange(row, group) for (row, group) in rows]))
