# global cache
#
# cache = {}
#
# def arrange(row, groups):
#     if (row, "".join([str(x) for x in groups])) in cache.keys():
#         return cache[(row, "".join([str(x) for x in groups]))]
#
#     row = row.lstrip(".")
#
#     if row == "":
#         return int(len(groups) == 0)
#
#     if len(groups) == 0:
#         return int(row.find("#") == -1)
#
#     if row[0] == "#":
#         ##Not enough row left or . in first group length
#         if len(row) < groups[0] or "." in row[:groups[0]]:
#             return 0
#
#         ##Row is same length as first group
#         elif len(row) == groups[0]:
#             return int(len(groups) == 1)
#
#         ##Invalid no gap between groups
#         elif row[groups[0]] == "#":
#             return 0
#
#         else:
#             ret = cache[(row[groups[0] + 1:], "".join("".join([str(x) for x in groups[1:]])))] if (row[groups[0] + 1:], "".join("".join([str(x) for x in groups[1:]]))) in cache.keys() else arrange(row[groups[0] + 1:], groups[1:])
#             cache[(row[groups[0] + 1:], "".join("".join([str(x) for x in groups[1:]])))] = ret
#             return ret
#
#     ret1 = cache[("#" + row[1:], "".join([str(x) for x in groups]))] if ("#" + row[1:], "".join([str(x) for x in groups])) in cache.keys() else arrange("#" + row[1:], groups)
#     ret2 = cache[(row[1:], "".join([str(x) for x in groups]))] if (row[1:], "".join([str(x) for x in groups])) in cache.keys() else arrange(row[1:], groups)
#
#     cache[("#" + row[1:], "".join([str(x) for x in groups]))] = ret1
#     cache[row[1:], "".join([str(x) for x in groups])] = ret2
#
#     return ret1 + ret2
#
# rows = []
#
# with open("test.txt", "r") as file:
#     rows += [[line.strip().split()[0], [int(x) for x in line.strip().split()[1].split(",")]] for line in file]
#
# for i, row in enumerate(rows):
#     rows[i][0] = ((row[0] + "?") * 5)[:-1]
#     rows[i][1] = rows[i][1] * 5
#
# print(cache)
# print(sum([arrange(row, group) for (row, group) in rows]))

from functools import cache


@cache
def arrange(row, groups):
    row = row.lstrip(".")

    if row == "":
        return int(len(groups) == 0)

    if len(groups) == 0:
        return int(row.find("#") == -1)

    groups = [int(x) for x in groups.split(",")]

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
            return arrange(row[groups[0] + 1:], ",".join(str(x) for x in groups[1:]))

    return arrange("#" + row[1:], ",".join(str(x) for x in groups)) + arrange(row[1:], ",".join(str(x) for x in groups))

rows = []

with open("Input.txt", "r") as file:
    rows += [line.strip().split() for line in file]

for i, row in enumerate(rows):
    rows[i][0] = ((row[0] + "?") * 5)[:-1]
    rows[i][1] = ((rows[i][1] + ",") * 5)[:-1]

print(sum([arrange(row, group) for (row, group) in rows]))
