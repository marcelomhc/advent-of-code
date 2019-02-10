import sys
import heapq

def part1(filepath):
    points = parse(filepath)
    
    points = sorted(points)
    const = [-1 for i in range(len(points))]
    const[0] = 0
    next_const = 0

    for i in range(len(points)):
        stars = set()
        curr_const = -1
        for j in range(i, len(points)):
            if(points[j][0] - points[i][0] > 3):
                break
            if(d3(points[i], points[j]) <= 3):
                if(const[j] != -1):
                    if( curr_const == -1):
                        curr_const = const[j]
                    const = merge(const, j, curr_const)
                stars.add(j)
        if(curr_const == -1):
            next_const += 1
            curr_const = next_const
        for idx in stars:
            const[idx] = curr_const
    print(const)
    print(len(set(const)))

def merge(constellations, idx, k):
    v = constellations[idx]
    for i in range(len(constellations)):
         if (constellations[i] == v):
            constellations[i] = k
    return constellations       

def d3(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1]) + abs(a[2]-b[2]) + abs(a[3]-b[3])


def parse(filepath):
    with open(filepath, 'r') as f:
        return [tuple(map(int, l.split(','))) for l in f.readlines()]

if __name__ == "__main__":
    part1(sys.argv[1])