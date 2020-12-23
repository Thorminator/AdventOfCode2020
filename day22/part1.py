def parse_input(file_name):
    with open(file_name) as f:
        inputs = f.read().split("\n\n")
        result = []
        for player_cards in inputs:
            result.append([int(n) for n in player_cards.splitlines()[1:]])
        return result


decks = parse_input("input.txt")
player1 = decks[0]
player2 = decks[1]
while len(player1) > 0 and len(player2) > 0:
    card1, card2 = player1.pop(0), player2.pop(0)
    if card1 > card2:
        player1.append(card1)
        player1.append(card2)
    else:
        player2.append(card2)
        player2.append(card1)
winner = player1 if len(player1) > 0 else player2
print(sum((len(winner) - i) * n for i, n in enumerate(winner)))
