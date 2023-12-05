cards = {}
total = 0

with open("Input.txt", "r") as file:
    for line in file:
        card, line = line.split(":")
        card = int(card.split(" ")[-1])

        if card in cards.keys():
            cards[card] += 1

        else:
            cards[card] = 1

        line = line.strip().split(" ")

        winning = [int(x) for x in line[:line.index("|")] if x != ""]
        numbers = [int(x) for x in line[line.index("|") + 1 :] if x != ""]

        winners = 0
        for num in numbers:
            if num in winning:
                winners += 1

        for i in range(winners):
            if i + card + 1 in cards.keys():
                cards[i + card + 1] += cards[card]

            else:
                cards[i + card + 1] = cards[card]

print(sum(cards.values()))
