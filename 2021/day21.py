from collections import deque


def part1(init1, init2):
    player1 = deque(range(10, 0, -1))
    player1.rotate(init1)
    player2 = deque(range(10, 0, -1))
    player2.rotate(init2)

    positions = deque([player1, player2])
    points = deque([0, 0])
    dice = deque(range(1, 101))
    rolls = 0
    while max(points) < 1000:
        for _ in range(3):
            rolls += 1
            positions[0].rotate(dice[0])
            dice.rotate(-1)
        points[0] += positions[0][0]
        positions.rotate()
        points.rotate()
    print(min(points)*rolls)


def calculate_move(position):
    new_position = []
    for dice, count in [(3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)]:
        new_position.append(((dice+position) % 10 if dice+position != 10 else 10, count))
    return new_position


def simulate_universes(play_status, curr_player, cache):
    calculated = cache.get((play_status, curr_player), None)
    if calculated:
        return calculated

    (_, points_1), (_, points_2) = play_status
    if points_1 > 20:
        return 1, 0
    if points_2 > 20:
        return 0, 1

    p1 = p2 = 0
    play_status_list = list(play_status)
    pos, points = play_status_list[curr_player]
    for move, count in calculate_move(pos):
        play_status_list[curr_player] = (move, points+move)
        s1, s2 = simulate_universes(tuple(play_status_list), (curr_player+1) % 2, cache)
        p1 += s1*count
        p2 += s2*count

    cache[(play_status, curr_player)] = (p1, p2)
    return p1, p2


def part2(init1, init2):
    wins = simulate_universes(((init1, 0), (init2, 0)), 0, dict())
    print(max(wins))


if __name__ == '__main__':
    part1(1, 2)
    part2(1, 2)
