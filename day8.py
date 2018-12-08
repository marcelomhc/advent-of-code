import sys
import re

def part1(stack):
    child = stack.pop(0)
    meta = stack.pop(0)

    total = 0
    for i in range(child):
        total += part1(stack)
    for j in range(meta):
        total += stack.pop(0)
    return total

def part2(stack):
    child = stack.pop(0)
    meta = stack.pop(0)

    total = 0
    childs = list()
    for i in range(child):
        childs.append(part2(stack))
    for j in range(meta):
        if(child == 0):
            total += stack.pop(0)
        else:
            idx = stack.pop(0)
            if not (idx == 0 or idx > len(childs)):
                total += childs[idx-1]
    return total

def main(filepath):
    stack = parse_input(filepath)
    #print(part1(stack))
    print(part2(stack))

def parse_input(filepath):
    with open(filepath, "r") as f:
        input = f.readline()
        return map(int, input.split(" "))

if __name__ == "__main__":
    main(sys.argv[1])