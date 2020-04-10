from collections import deque, defaultdict

def part1(players, marbles):
    board = [0, 4, 2, 5, 1, 6, 3, 7]
    player = 8
    curr = 7
    points = dict()

    for marble in range(8, marbles+1):
        if (marble % 23 == 0):
            curr = curr - 7
            if (curr < 0):
                curr = curr + len(board)
            left = board[curr]
            board.pop(curr)
            points[player] = points.setdefault(player, 0) + marble + left
        else:
            curr = (curr + 2) % len(board)
            board.insert(curr, marble)
        player = (player + 1) % players
    print(max(points.values()))
    #print(board)

def part2(players, marbles):
    points = defaultdict(int)
    board = deque([0])

    for marble in range(1, marbles+1):
        if marble % 23 == 0:
            board.rotate(7)
            points[marble % players] += marble + board.pop()
            board.rotate(-1)
        else:
            board.rotate(-1)
            board.append(marble)
    print(max(points.values()))

if __name__ == "__main__":
    part2(9, 25)
    part2(10, 1618)
    part2(13, 7999)
    part2(17, 1104)
    part2(412, 71646)
    part2(412, 7164600)