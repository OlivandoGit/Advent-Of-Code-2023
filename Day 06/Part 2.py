with open("Input.txt", "r") as file:
    lines = file.readlines()

lines = [[x for x in line.strip().split(":")[1].split(" ") if x != ""] for line in lines]

time, record = [int("".join(line)) for line in lines]

wins = 0
for i in range((time + 1) // 2):
    if i * (time - i) > record:
        wins = ((time + 1) // 2) - i
        break

print((wins * 2) + (1 if time % 2 == 0 else 0))
