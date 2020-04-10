import sys
from collections import defaultdict

class Room(object):
    def __init__(self):
        self.N = None
        self.E = None
        self.W = None
        self.S = None
        self.visited = False

class Node(object):
    edges = list()


def part1(filepath):
    with open(filepath, 'r') as f:
        line = f.readline()[1:-1]
        print(line)
    
    graph = buildDigraph(line)
    rooms = defaultdict(Room)
    rooms[(0,0)] = Room()
    visited = defaultdict(bool)
    dfs(graph, line, rooms, 0, 0, 0, visited)
    bfs(rooms[(0,0)])

def dfs(graph, line, rooms, i, x, y, visited):
    if(visited[(x,y,i)]):
        return
    visited[(x,y,i)] = True
    while(True):
        if (i >= len(line)):
            return
        char = line[i]
        curr = rooms[(x,y)]
        if(char == 'N'):
            y += 1
        elif(char == 'S'):
            y -= 1
        elif(char == 'E'):
            x += 1
        elif(char == 'W'):
            x -= 1
        else:
            for n in graph[i]:
                dfs(graph, line,rooms, n, x, y, visited)
            return

        idx = (x,y)
        nextRoom = rooms[idx]
        setattr(curr, char, nextRoom)
        setattr(nextRoom, opos(char), curr)
        if (len(graph[i]) > 1):
            for n in graph[i]:
                dfs(graph, line,rooms, n, x, y, visited)
                return
        i = list(graph[i])[0]

def opos(char):
    chars = ['N', 'E', 'S', 'W']
    idx = (chars.index(char) + 2 ) % 4
    return chars[idx]

def bfs(room):
    queue = list()
    queue.append((0, room))

    maxDeep = 0
    total = 0

    while(len(queue) > 0):
        deep, curr = queue.pop(0)
        if not (curr.visited):
            if(deep > 999):
                total += 1
            curr.visited = True
            if(deep > maxDeep):
                maxDeep = deep
            if(curr.N != None):
                queue.append((deep+1, curr.N))
            if(curr.S != None):
                queue.append((deep+1, curr.S))
            if(curr.W != None):
                queue.append((deep+1, curr.W))
            if(curr.E != None):
                queue.append((deep+1, curr.E))
    print(maxDeep)
    print(total)

def buildDigraph(re):
    ops = list()
    graph = [set() for _ in range(len(re))]
    for i in range(len(re)):
        if(re[i] == '('):
            ops.append(i)
        elif (re[i] == '|'):
            ops.append(i)
            continue
        elif(re[i] == ')'):
            lp = ops.pop()
            ors = list()
            while(re[lp] == '|'):
                graph[lp].add(i)
                ors.append(lp)
                lp = ops.pop()
            for op in ors:
                graph[lp].add(op+1)

        graph[i].add(i+1)
        i += 1
    print(ops)
    return graph

if __name__ == "__main__":
    part1(sys.argv[1])