def part1(bingo):
    numbers, boards = bingo
    calculate_score(boards, numbers)


def part2(bingo):
    numbers, boards = bingo
    calculate_score(boards, numbers, False)


def calculate_score(boards, numbers, find_winner=True):
    for number in numbers:
        winners = []
        for row_marks, col_marks, board in boards:
            board_position = board.pop(number, None)
            if board_position:
                row, col = board_position
                row_marks[row] += 1
                col_marks[col] += 1

                if row_marks[row] == 5 or col_marks[col] == 5:
                    if find_winner:
                        print(sum(board.keys()) * number)
                        return
                    else:
                        if len(boards) == 1:
                            print(sum(board.keys()) * number)
                            return
                        winners.append((row_marks, col_marks, board))
        for winner in winners:
            boards.remove(winner)


def get_bingo(filepath):
    with open(filepath, 'r') as f:
        boards = []
        board = {}
        lines = f.readlines()
        numbers = list(map(int, lines[0].strip().split(',')))

        row = 0
        for line in lines[2:]:
            if line == '\n':
                boards.append(([0 for _ in range(row)], [0 for _ in range(col)], board))
                board = {}
                row = 0
            else:
                col = 0
                for n in list(map(int, line.strip().split())):
                    board[n] = (row, col)
                    col += 1
                row += 1
        boards.append(([0 for _ in range(row)], [0 for _ in range(col)], board))
    return numbers, boards


if __name__ == "__main__":
    part1(get_bingo("input/day04.data"))
    part2(get_bingo("input/day04.data"))
