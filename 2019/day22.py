from collections import deque

def get_instructions(filepath):
    inst = list()
    with open(filepath, "r") as f:
        for line in f:
            if(line.startswith('deal into')):
                inst.append(('S', 0))
                continue
            words = line.strip().split(' ')
            if(line.startswith('deal with')):
                inst.append(('I', int(words[-1])))
            else:
                inst.append(('C', int(words[-1])))

        return(inst)

def shuffle(instructions, cards):
    deck = [x for x in range(cards)]
    for instruction, value in instructions:
        if(instruction == 'S'):
            deck = stack(deck)
        elif(instruction == 'I'):
            deck = increment(deck, value)
        else:
            deck = cut(deck, value)

    print(deck.index(2019))

def stack(deck):
    return list(reversed(deck))

def cut(deck,cut):
    deck = deque(deck)
    deck.rotate(cut*-1)
    return list(deck)

def increment(deck, inc):
    new = [-1]*len(deck)
    pos = 0
    for card in deck:
        new[pos] = card
        pos = (pos+inc) % len(deck)
    return new

def solve(c, n, p, o=0, i=1):
    inv = lambda x: pow(x, c-2, c)
    for s in [s.split() for s in open('input/day22.data').readlines()]:
        if s[0] == 'cut':  o += i * int(s[-1])
        if s[1] == 'with': i *= inv(int(s[-1]))
        if s[1] == 'into': o -= i; i *= -1
    o *= inv(1-i)
    i = pow(i, n, c)
    return (p*i + (1-i)*o) % c

if __name__ == "__main__":

    instructions = get_instructions("input/day22.data")
    shuffle(instructions, 10007)
    print(solve(119315717514047,101741582076661,2020))