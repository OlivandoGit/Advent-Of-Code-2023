total = 0

with open("Input.txt", "r") as file:
    for line in file:
        numbers = list(filter(lambda chr: chr.isdigit(), list(line.strip())))
        
        total += int(numbers[0] + numbers[-1])

print(total)
