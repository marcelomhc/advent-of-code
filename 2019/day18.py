from functools import lru_cache

def parse(filepath, recursion=False):
    with open(filepath, 'r') as f:
        lines = f.read().splitlines()

        grid = dict()
        keys = set()

        for y in range(len(lines)):
            for x in range(len(lines[y])):
                char = lines[y][x]
                if(char == '@'):
                    src = (x,y)
                    grid[(x,y)] = '.'
                else:
                    grid[(x,y)] = char
                if('a' <= char <= 'z'):
                    keys.add((x,y))
    return grid, src, keys

def get_neighboors(position):
    x,y = position
    return [(x-1,y), (x+1, y), (x, y-1), (x,y+1)]

def collect():
    board, src, keys = parse('input/day18.data')
    distances = get_distances(keys, src, board)
    print(search(board, src, len(keys), distances, frozenset()))

def parallel():
    board, src, keys = parse('input/day18.data')
    entrances = split_board(board, src, keys)
    steps = 0
    for entrance, collected in entrances:
        required = keys.difference(collected)
        distances = get_distances(required, entrance, board)
        steps += search(board, entrance, len(keys), distances, frozenset([board[k] for k in collected]))
    print(steps)

def split_board(board, src, keys):
    x,y = src
    board[src] = '#'
    entrances = []
    for pos in get_neighboors(src):
        board[pos] = '#'
    for pos in [(x-1, y-1), (x+1, y-1), (x-1, y+1), (x+1, y+1)]:
        entrances.append((pos, keys.difference(sub_keys(pos, board))))
    return entrances

def sub_keys(pos, board):
    midX = max(board.keys(), key=lambda l: l[0])[0]//2
    midY = max(board.keys(), key=lambda l: l[1])[1]//2

    present = set()
    x,y = pos
    for j in range(midY):
        for i in range(midX):
            pi = i+(x > midX)*midX
            pj = j+(y > midY)*midY
            if('a' <= board[(pi,pj)] <= 'z'):
                present.add((pi,pj))
    return present

def get_distances(keys, src, board):
    dist = dict()
    origins = keys.copy()
    origins.add(src)
    for _from in origins:
        dist[_from] = dict()
        for to in keys:
            dist[_from][to] = bfs(board, _from, to)

    return dist

def search(board, src, n, distances, collected):

    @lru_cache(maxsize=10000000)
    def search_(src, collected):
        if(len(collected) == n):
            return 0

        minSteps = 99999999999

        for key in distances[src]:
            if(board[key] not in collected):
                dist, doors = distances[src][key]
                if(doors.issubset(collected)):
                    steps = search_(key, collected.union(board[key])) + dist
                    minSteps = min(steps, minSteps)

        return minSteps

    minSteps = search_(src, collected)
                        # queue.append((steps+dist, key, collected.union(board[key])))
    return minSteps

def bfs(board, src, dst):
    if(src == dst):
        return (0, {})
    queue = list()
    queue.append((0, src, set()))
    visited = set()

    while(len(queue) > 0):
        steps, src, doors = queue.pop(0)
        if(src not in visited):
            visited.add(src)
            for neighboor in get_neighboors(src):
                if(neighboor == dst):
                    return (steps+1, doors)
                pixel = board[neighboor]
                if('A' <= pixel <= 'Z'):
                    _doors = doors.copy()
                    _doors.add(pixel.lower())
                    queue.append((steps + 1, neighboor, _doors))
                elif(pixel != '#'):
                    queue.append((steps + 1, neighboor, doors))

if __name__ == "__main__":
    collect()
    parallel()
