def compare(hand1, hand2):
    for i, card in enumerate(hand1):
        if card > hand2[i]:
            return 1

        if card < hand2[i]:
            return -1

    return 0

cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
counts = []

with open("Input.txt", "r") as file:
    for line in file:
        count = []
        hand, bid = line.strip().split(" ")

        for card in cards:
            if hand.count(card) > 0:
                count.append(hand.count(card))

        hand = [(len(cards) - cards.index(chr)) - 1 for chr in hand]

        counts.append((hand, count, int(bid)))

types = [lambda x: max(x) == 5, lambda x: max(x) == 4, lambda x: max(x) == 3 and max(x[:x.index(3)] + x[x.index(3) + 1:]) == 2, lambda x: max(x) == 3, lambda x: max(x) == 2 and max(x[:x.index(2)] + x[x.index(2) + 1:]) == 2, lambda x: max(x) == 2, lambda x: max(x) == 1]

typesList = [[] for i in range(7)]

for count in counts:
    for i, t in enumerate(types):
        if t(count[1]):
            typesList[i].append(count)
            break

for tlist in typesList:
    for i in range(len(tlist) - 1):
        for j in range(len(tlist) - 1):
            if compare(tlist[j][0], tlist[j + 1][0]) == -1:
                temp = tlist[j + 1]

                tlist[j + 1] = tlist[j]
                tlist[j] = temp

rank = len(counts)
total = 0

for tlist in typesList:
    for count in tlist:
        total += count[2] * rank
        rank -= 1

print(total)
