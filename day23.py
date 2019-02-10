import re, sys
import heapq

def part1(filepath):
    nano = parse(filepath)
    nano = sorted(nano, key= lambda l: l[3], reverse=True)
    r = nano[0]
    print('radius: ' + str(r[3]))
    inr = 0
    for robot in nano:
        inr += int(d3(robot, r) <= r[3])
    print(inr)

def part2(filepath):
    nanobots = parse(filepath)

    heap = initialize_heap(nanobots)

    while(heap):
        neg_reach, neg_size, dist, box = heapq.heappop(heap)
        if(neg_size == -1):
            print("Found box with %s distance and in range of %s bots" %
                (str(dist), str(-neg_reach)))
            print(box)
            break

        new_size = neg_size // -2
        for octant in [(0,0,0), (0,0,1), (0,1,0), (0,1,1), 
                        (1,0,0), (1,0,1), (1,1,0), (1,1,1)]:
            min_corner = tuple(box[0][i] + new_size*octant[i] for i in (0,1,2))
            max_corner = tuple(min_corner[i] + new_size for i in (0,1,2))
            new_box = (min_corner, max_corner)
            new_reach = get_intersects(new_box, nanobots)
            heapq.heappush(heap, (-new_reach, -new_size, d3(min_corner, (0,0,0)), new_box))

def get_intersects(box, bots):
    return sum(1 for bot in bots if does_intersect(box, bot))

def does_intersect(box, bot):
    (min_corner, max_corner) = box
    d = 0
    for i in (0,1,2):
        d += abs(bot[i] - min_corner[i]) + abs(bot[i] - max_corner[i]+1) - (max_corner[i] -1 - min_corner[i])
    d //= 2
    return d <= bot[3]

def initialize_heap(bots):
    max_size = max(max(abs(b[i]) + b[3] for b in bots) for i in (0,1,2))
    box_size = 1
    while (max_size >= box_size):
        box_size *= 2
    # Negate size and number of bots contained to prioritaze the max of those
    # Do not negate distance as we want the minimum
    # Box = (minX, minY, minZ), (maxX, maxY, maxZ) ==> (min_corner, max_corner)
    return [ (-len(bots), -2*box_size, 3*box_size, ((-box_size, -box_size, -box_size), (box_size, box_size, box_size)))]

def d3(a , b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])

def parse(filepath):
    nanobots = list()
    with open(filepath, 'r') as f:
        for line in f.readlines():
            n = re.match('pos=<(-*\d+),(-*\d+),(-*\d+)>, r=(\d+)', line)
            nanobots.append(tuple(map(int, n.groups())))
        return nanobots

if __name__ == "__main__":
    part1(sys.argv[1])
    part2(sys.argv[1])