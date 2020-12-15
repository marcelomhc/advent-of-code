def game(starting, rounds):
    spoken = {num: i + 1 for i, num in enumerate(starting[:-1])}
    last = starting[-1]

    for i in range(len(starting), rounds):
        spoken[last], last = (i, i - spoken[last]) if spoken.get(last) else (i, 0)
    print(last)


if __name__ == "__main__":
    start = [20, 0, 1, 11, 6, 3]
    game(start, 2020)
    game(start, 30000000)
