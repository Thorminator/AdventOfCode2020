def parse_input(file_name):
    with open(file_name) as f:
        inputs = f.read().split("\n\n")
        result = []
        for player_cards in inputs:
            result.append([int(n) for n in player_cards.splitlines()[1:]])
        return result


def can_recurse(card1, player1, card2, player2):
    return len(player1) > card1 and len(player2) > card2


def recursive_combat(player1, player2):
    prev_player1 = set()
    prev_player2 = set()
    while len(player1) > 0 and len(player2) > 0:
        player1_tuple = tuple(n for n in player1)
        player2_tuple = tuple(n for n in player2)
        if player1_tuple in prev_player1 and player2_tuple in prev_player2:
            return 0

        prev_player1.add(player1_tuple)
        prev_player2.add(player2_tuple)
        card1, card2 = player1[0], player2[0]
        if can_recurse(card1, player1, card2, player2):
            winner = recursive_combat(player1[1:card1 + 1], player2[1:card2 + 1])
        else:
            winner = 0 if card1 > card2 else 1
        if winner == 0:
            player1.append(player1.pop(0))
            player1.append(player2.pop(0))
        else:
            player2.append(player2.pop(0))
            player2.append(player1.pop(0))
    return 0 if len(player1) > 0 else 1


decks = parse_input("input.txt")
res = recursive_combat(decks[0], decks[1])
winning_deck = decks[res]
print(sum((len(winning_deck) - i) * n for i, n in enumerate(winning_deck)))
