with open("Input.txt", "r") as file:
    lines = file.readlines()

times, records = [[int(x) for x in line.strip().split(":")[1].split(" ") if x != ""] for line in lines]

total = 1

for x, time in enumerate(times):
    wins = 0
    for i in range(time + 1):
        if i * (time - i) > records[x]:
            wins += 1

    total *= wins

print(total)
