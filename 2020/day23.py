from collections import deque


def get_destination(selected, pick, top):
    while True:
        selected -= 1
        if selected == 0:
            selected = top
        if selected not in pick:
            return selected


def play(cups, rounds):
    top = max(cups)
    cups = deque(cups)
    for _ in range(rounds):
        pick = []
        cups.rotate(-1)
        for _ in range(3):
            pick.append(cups.popleft())
        cups.rotate(1)

        idx = cups.index(get_destination(cups[0], pick, top)) + 1

        for cup in reversed(pick):
            cups.insert(idx, cup)
        cups.rotate(-1)

    while cups[0] != 1:
        cups.rotate(-1)
    cups.popleft()
    print(''.join([str(cup) for cup in cups]))


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def play2(cups, rounds):
    location = {}
    top = max(cups)

    initial = cups[0]
    prev = Node(initial)
    location[initial] = prev
    for cup in cups[1:]:
        new_cup = Node(cup)
        prev.next = new_cup
        prev = new_cup
        location[cup] = new_cup

    curr = location.get(initial)
    prev.next = curr

    for _ in range(rounds):
        pick = []

        p = curr.next
        for _ in range(3):
            pick.append(p.value)
            p = p.next
        curr.next = p

        left = location[get_destination(curr.value, pick, top)]
        right = left.next
        left.next = location.get(pick[0])
        location.get(pick[2]).next = right
        curr = curr.next

    cup = location.get(1)

    result = 1
    for _ in range(2):
        result *= cup.next.value
        cup = cup.next
    print(result)


if __name__ == "__main__":
    c = [4, 6, 9, 2, 1, 7, 5, 3, 8]
    play(c, 100)

    c.extend([i for i in range(10, 1000000+1)])
    play2(c, 10000000)
