from collections import deque
from itertools import repeat, accumulate
from functools import reduce

def parse_program(filepath):
    with open(filepath, "r") as f:
        program = list(map(int, [char for char in f.readline()]))
    return program

def fft(number):
    for _ in range(100):
        number = phase(number)
    print(number[0:8])

def phase(number):
    result = []
    for i in range(len(number)):
        pattern = deque([x for item in [0,1,0,-1] for x in repeat(item, i+1)])
        pattern.rotate(-1)
        result.append(calculate(number, pattern))
    return result

def fft_offset(number, offset):
    offset = reduce(lambda total, d: 10 * total + d, data[:offset], 0)
    number = number * 10000
    number = number[offset:]

    number = reversed(number)
    for _ in range(100):
        number = accumulate(number, lambda a, b: (a + b) % 10)
    number = list(reversed(list(number)))

    print(number[:8])

def calculate(number, pattern):
    total = 0
    for digit in number:
        total += digit*pattern[0]
        pattern.rotate(-1)
    return abs(total) % 10

if __name__ == "__main__":
    data = parse_program("input/day16.data")
    fft(data)
    fft_offset(data, 7)