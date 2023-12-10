histories = []
with open("Input.txt", "r") as file:
    histories = [[int(x) for x in line.strip().split()] for line in file]

for history in histories:
    sequences = [history]

    while sum(x != 0 for x in sequences[-1]) != 0:
        sequence = []
        for i, num in enumerate(sequences[-1][:-1]):
            sequence.append(sequences[-1][i + 1] - num)

        sequences.append(sequence)

    for i, sequence in enumerate(sequences[::-1][:-1]):
        sequences[len(sequences) - i - 2].append(sequences[len(sequences) - i - 2][-1] + sequence[-1])
        
print(sum([history[-1] for history in histories]))
