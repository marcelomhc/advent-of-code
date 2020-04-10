import sys
import re

def main(filepath):
    stack = parse_input(filepath)
    sizes = dict()
    for i in range(26):
        unit = chr(i+97)
        cleaned = clean(stack, unit)
        print(unit + " " + str(len(cleaned)))
        sizes[unit] = len(cleaned)
    cleaned = clean(stack, ' ')
    print("Base case: " + str(len(cleaned)))
    sizes[' '] = len(cleaned)

    s = sorted(sizes.items(), key=lambda obj:(obj[1]))
    print(s[0])

def parse_input(filepath):
    stack = []
    
    with open(filepath, "r") as f:
        input = f.readline()
        for letter in input:
            stack.append(letter)
        stack.pop()
    return stack

def clean(input, unit):
    stack = []
    for letter in input:
        if(letter.lower() == unit):
            continue
        elif(len(stack) == 0):
            stack.append(letter)
        elif (abs(ord(letter) - ord(stack[-1])) == 32):
            stack.pop()
        else:
            stack.append(letter)
    return stack

if __name__ == "__main__":
    main(sys.argv[1])