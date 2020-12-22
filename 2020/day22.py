def parse(filepath):
    with open(filepath, 'r') as f:
        decks = []
        for player in f.read().split('\n\n'):
            name, *cards = player.splitlines()
            decks.append([int(card) for card in cards])
    return decks


def play(decks):
    player1, player2 = decks
    while len(player1) > 0 and len(player2) > 0:
        card1 = player1.pop(0)
        card2 = player2.pop(0)

        if card1 > card2:
            player1.extend([card1, card2])
        else:
            player2.extend([card2, card1])
    return player1, player2


def recursive(decks):
    player1, player2 = decks
    rounds = set()
    while len(player1) > 0 and len(player2) > 0:
        p1 = str(player1)
        p2 = str(player2)
        if (p1, p2) in rounds:
            return ['winner'], []

        rounds.add((p1, p2))

        card1 = player1.pop(0)
        card2 = player2.pop(0)

        if len(player1) >= card1 and len(player2) >= card2:
            r1, r2 = recursive([player1[0:card1], player2[0:card2]])
            if len(r1) > len(r2):
                player1.extend([card1, card2])
            else:
                player2.extend([card2, card1])
        else:
            if card1 > card2:
                player1.extend([card1, card2])
            else:
                player2.extend([card2, card1])

    return player1, player2


def get_points(decks):
    player1, player2 = decks
    player1.extend(player2)
    winner = enumerate(reversed(player1))
    result = 0
    for i, card in winner:
        result += (i + 1) * card
    print(result)


if __name__ == "__main__":
    get_points(play(parse("input/day22.data")))
    get_points(recursive(parse("input/day22.data")))
