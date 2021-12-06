from collections import deque


def lanternfish(fish_list, d):
    days = [0 for _ in range(9)]
    for fish in fish_list:
        days[fish] += 1
    days = deque(days)

    for _ in range(d):
        days.rotate(-1)
        days[6] += days[8]
    print(sum(days))


if __name__ == "__main__":
    with open("input/day06.data", 'r') as f:
        initial_fish = list(map(int, f.readline().split(',')))
    lanternfish(initial_fish, 80)
    lanternfish(initial_fish, 256)
